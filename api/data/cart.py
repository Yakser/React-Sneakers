import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


from .db_session import SqlAlchemyBase


class Cart(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'cart'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    item_id = sqlalchemy.Column('item_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('sneakers.id'))
    
    def __repr__(self):
        return f"<Cart> {self.id} {self.item_id}"
