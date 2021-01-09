from sqlalchemy import Column, Integer, String
from be.model.database import Base


class New_Order_Detail(Base):
    __tablename__ = 'new_order_detail'
    order_id = Column(String(240), primary_key=True)
    book_id = Column(String(240), primary_key=True)
    count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    # state 0:未付款 1:已付款 2：已发货 3：已收货
    state = Column(Integer, nullable=False)

    def __init__(self, order_id=None, book_id=None, count=None, price=None, state=0):
        self.order_id = order_id
        self.book_id = book_id
        self.count = count
        self.price = price
        self.state = state

    def __repr__(self):
        return '<User %r,%r,%r,%r,%r>' % (self.order_id, self.book_id, self.count, self.price, self.state)
