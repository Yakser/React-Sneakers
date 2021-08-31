from flask import jsonify, request
from flask_restful import Resource, abort

from data import db_session
from data.favorite import Favorite
from data.favorite_argparser import parser, edit_parser


class FavoriteResource(Resource):

    def get(self, favorite_id):
        abort_if_favorite_not_found(favorite_id)

        session = db_session.create_session()
        favorite = session.query(Favorite).filter(
            Favorite.item_id == favorite_id).all()[0]

        return jsonify({'favorite': favorite.to_dict(
            only=('id', 'item_id'))})

    def put(self, favorite_id):
        abort_if_favorite_not_found(favorite_id)
        try:
            args = edit_parser.parse_args()
            session = db_session.create_session()
            favorite = session.query(Favorite).filter(
                Favorite.item_id == favorite_id).all()[0]
            favorite.item = args.get('item_id', favorite.item)
            session.commit()
        except Exception:
            return jsonify({'error': 'Incorrect data'})
        return jsonify({'success': 'OK'})

    def delete(self, favorite_id):
        abort_if_favorite_not_found(favorite_id)
        session = db_session.create_session()
        favorite = session.query(Favorite).filter(
            Favorite.item_id == favorite_id).all()[0]
        session.delete(favorite)
        session.commit()
        return jsonify({'success': 'OK'})


class FavoriteListResource(Resource):

    def get(self):

        args = dict(request.args)
        page = int(args.get('page', 1))
        count = int(args.get('count', 12))
        session = db_session.create_session()
        favorite = session.query(Favorite).all()
        total_count = len(favorite)
        pages = {}

        for i, favorite in enumerate(favorite):
            if i // count in pages:
                pages[i // count] += [favorite]
            else:
                pages[i // count] = [favorite]

        favorite = pages.get(page - 1, [])

        return jsonify({'favorite': [item.to_dict(
            only=('id', 'item_id')) for item
            in favorite], 'totalCount': total_count})

    def post(self):
        try:
            args = parser.parse_args()
            session = db_session.create_session()

            favorite = Favorite(
                item_id=args['item_id']
            )
            session.add(favorite)
            session.commit()
            return jsonify({'success': 'OK', 'favorite_id': favorite.item_id})
        except Exception:
            return jsonify({'error': 'Favorite already exists or data is incorrect'})


def abort_if_favorite_not_found(favorite_id):

    session = db_session.create_session()
    favorite = None
    try:
        favorite = session.query(Favorite).filter(
            Favorite.item_id == favorite_id).all()[0]
    except Exception:
        if not favorite:
            abort(404, message=f"Favorite {favorite_id} not found")
