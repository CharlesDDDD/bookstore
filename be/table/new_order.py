from sqlalchemy import Column, Text, String
from be.model.database import Base


class New_Order(Base):
    __tablename__ = 'new_order'
    order_id = Column(String(240), primary_key=True)
    user_id = Column(String(240), unique=True)
    store_id = Column(String(240), nullable=False)

    def __init__(self, order_id=None, user_id=None, store_id=None):
        self.order_id = order_id
        self.user_id = user_id
        self.store_id = store_id

    def __repr__(self):
        return '<User %r,%r,%r>' % (self.order_id, self.user_id, self.store_id)
