from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash

from data import db_session
from data.user import User
from data.users_argparser import parser, edit_parser


class UserResource(Resource):
    """
        Ресурс User для одного объекта
        Осуществляет получение, изменение и удаление пользователей
    """

    def get(self, user_id):
        abort_if_user_not_found(user_id)

        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'login', 'password', 'name', 'surname',
                  'sex', 'country', 'city', 'phone', 'email', 'avatar_url'))})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        try:

            args = edit_parser.parse_args()
            session = db_session.create_session()
            user = session.query(User).get(user_id)
            user.name = args.get('name', user.name)
            user.surname = args.get('surname', user.surname)
            user.sex = args.get('sex', user.sex)
            user.country = args.get('country', user.country)
            user.city = args.get('city', user.city)
            user.phone = args.get('phone', user.phone)
            session.commit()
        except Exception:
            return jsonify({'error': 'Incorrect data'})
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    """
        Ресурс Note для списка объектов
        Осуществляет получение и добавление пользователей
    """

    def get(self):

        args = dict(request.args)
        page = int(args.get('page', 1))
        count = int(args.get('count', 10))
        session = db_session.create_session()
        users = session.query(User).all()
        total_count = len(users)
        pages = {}

        for i, user in enumerate(users):
            if i // count in pages:
                pages[i // count] += [user]
            else:
                pages[i // count] = [user]

        users = pages.get(page - 1, [])

        return jsonify({'users': [item.to_dict(
            only=('id', 'login', 'password', 'name', 'surname',
                  'sex', 'country', 'city', 'phone', 'email', 'avatar_url')) for item
            in users], 'totalCount': total_count})

    def post(self):
        try:
            args = parser.parse_args()
            session = db_session.create_session()
            user = User(
                login=args['login'],
                password=generate_password_hash(args['password']),
                name=args['name'],
                surname=args['surname'],
                sex=args['sex'],
                country=args['country'],
                city=args['city'],
                phone=args['phone'],
                email=args['email'],
                modified_date=args['modified_date'])

            session.add(user)
            session.commit()
            return jsonify({'success': 'OK', 'user_id': user.id})
        except Exception:
            return jsonify({'error': 'User already exists or data is incorrect'})


def abort_if_user_not_found(user_id):
    """ Вызывает abort(404), если происходит обращение к несуществующему пользователю"""
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
#
# users_resource
# # Created by Sergey Yaksanov at 26.08.2021
# Copyright © 2020 Yakser. All rights reserved.
