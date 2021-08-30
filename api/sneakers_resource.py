from flask import jsonify, request
from flask_restful import Resource, abort

from data import db_session
from data.sneakers import Sneakers
from data.sneakers_argparser import parser, edit_parser


class SneakersResource(Resource):
   
    def get(self, sneakers_id):
        abort_if_sneakers_not_found(sneakers_id)

        session = db_session.create_session()
        sneakers = session.query(Sneakers).get(sneakers_id)
        return jsonify({'sneakers': sneakers.to_dict(
            only=('id', 'title', 'price', 'image_url'))})

    def put(self, sneakers_id):
        abort_if_sneakers_not_found(sneakers_id)
        try:

            args = edit_parser.parse_args()
            session = db_session.create_session()
            sneakers = session.query(Sneakers).get(sneakers_id)
            sneakers.title = args.get('title', sneakers.title)
            sneakers.price = args.get('price', sneakers.price)
            sneakers.image_url = args.get('image_url', sneakers.image_url)
           
            session.commit()
        except Exception:
            return jsonify({'error': 'Incorrect data'})
        return jsonify({'success': 'OK'})

    def delete(self, sneakers_id):
        abort_if_sneakers_not_found(sneakers_id)
        session = db_session.create_session()
        sneakers = session.query(Sneakers).get(sneakers_id)
        session.delete(sneakers)
        session.commit()
        return jsonify({'success': 'OK'})


class SneakersListResource(Resource):

    def get(self):

        args = dict(request.args)
        page = int(args.get('page', 1))
        count = int(args.get('count', 12))
        session = db_session.create_session()
        sneakers = session.query(Sneakers).all()
        total_count = len(sneakers)
        pages = {}

        for i, sneakers in enumerate(sneakers):
            if i // count in pages:
                pages[i // count] += [sneakers]
            else:
                pages[i // count] = [sneakers]

        sneakers = pages.get(page - 1, [])

        return jsonify({'sneakers': [item.to_dict(
            only=('id', 'title', 'price', 'image_url')) for item
            in sneakers], 'totalCount': total_count})

    def post(self):
        try:
            args = parser.parse_args()
            session = db_session.create_session()
            sneakers = Sneakers(
                title=args['title'],
                price=args['price'], 
                image_url=args['image_url']
            )
            session.add(sneakers)
            session.commit()
            return jsonify({'success': 'OK', 'sneakers_id': sneakers.id})
        except Exception:
            return jsonify({'error': 'Sneakers already exists or data is incorrect'})


def abort_if_sneakers_not_found(sneakers_id):
   
    session = db_session.create_session()
    sneakers = session.query(Sneakers).get(sneakers_id)
    if not sneakers:
        abort(404, message=f"Sneakers {sneakers_id} not found")
