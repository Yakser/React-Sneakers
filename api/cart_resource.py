from flask import jsonify, request
from flask_restful import Resource, abort

from data import db_session
from data.cart import Cart
from data.cart_argparser import parser, edit_parser


class CartResource(Resource):
   
    def get(self, cart_id):
        abort_if_cart_not_found(cart_id)

        session = db_session.create_session()
        cart = session.query(Cart).get(cart_id)
        return jsonify({'cart': cart.to_dict(
            only=('id', 'item_id'))})

    def put(self, cart_id):
        abort_if_cart_not_found(cart_id)
        try:

            args = edit_parser.parse_args()
            session = db_session.create_session()
            cart = session.query(Cart).get(cart_id)
            cart.item = args.get('item_id', cart.item)
            session.commit()
        except Exception:
            return jsonify({'error': 'Incorrect data'})
        return jsonify({'success': 'OK'})

    def delete(self, cart_id):
        abort_if_cart_not_found(cart_id)
        session = db_session.create_session()
        cart = session.query(Cart).get(cart_id)
        session.delete(cart)
        session.commit()
        return jsonify({'success': 'OK'})


class CartListResource(Resource):

    def get(self):

        args = dict(request.args)
        page = int(args.get('page', 1))
        count = int(args.get('count', 12))
        session = db_session.create_session()
        cart = session.query(Cart).all()
        total_count = len(cart)
        pages = {}

        for i, cart in enumerate(cart):
            if i // count in pages:
                pages[i // count] += [cart]
            else:
                pages[i // count] = [cart]

        cart = pages.get(page - 1, [])

        return jsonify({'cart': [item.to_dict(
            only=('id', 'item_id')) for item
            in cart], 'totalCount': total_count})

    def post(self):
        try:
            args = parser.parse_args()
            session = db_session.create_session()
           
            cart = Cart(
               item_id=args['item_id']
            )
            
            session.add(cart)
            session.commit()
            return jsonify({'success': 'OK', 'cart_id': cart.id})
        except Exception:
            return jsonify({'error': 'Cart already exists or data is incorrect'})


def abort_if_cart_not_found(cart_id):
   
    session = db_session.create_session()
    cart = session.query(Cart).get(cart_id)
    if not cart:
        abort(404, message=f"Cart {cart_id} not found")
