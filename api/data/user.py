import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    """ Модель User - пользователь """
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    name = sqlalchemy.Column(sqlalchemy.String)
    surname = sqlalchemy.Column(sqlalchemy.String)
    sex = sqlalchemy.Column(sqlalchemy.String)
    country = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    avatar_url = sqlalchemy.Column(sqlalchemy.String)

    def set_password(self, password):
        """Хэширует и устанавливает пользователю пароль"""
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        """Проверяет пароль на правильность"""
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f"<User> {self.id} {self.surname} {self.name}"
