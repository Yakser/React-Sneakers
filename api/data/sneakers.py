import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


from .db_session import SqlAlchemyBase


class Sneakers(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'sneakers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    image_url = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    
    def __repr__(self):
        return f"<Sneakers> {self.id} {self.title}"
