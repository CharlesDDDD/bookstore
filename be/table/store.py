from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from be.model.database import Base


class Store(Base):
    __tablename__ = 'store'
    store_id = Column(String(240), primary_key=True)
    book_id = Column(String(240), primary_key=True)
    book_info = Column(LONGTEXT, nullable=True)
    stock_level = Column(Integer, nullable=True)
    title = Column(String(255))
    tag = Column(String(255))
    author = Column(String(255))
    content = Column(LONGTEXT, nullable=True)


    def __init__(self, store_id=None, book_id=None, book_info=None, title=None,tag=None,author=None,content=None,stock_level=None):
        self.store_id = store_id
        self.book_id = book_id
        self.book_info = book_info
        self.title = title
        self.tag = tag
        self.author = author
        self.content = content
        self.stock_level = stock_level

    def __repr__(self):
        return '<User %r,%r,%r,%r>' % (self.store_id, self.book_id, self.book_info, self.stock_level)
