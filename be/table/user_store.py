from sqlalchemy import Column, Integer, String, Text
from be.model.database import Base


class User_Store(Base):
    __tablename__ = 'user_store'
    user_id = Column(String(240), primary_key=True)
    store_id = Column(String(240), primary_key=True)

    def __init__(self, user_id=None, store_id=None):
        self.user_id = user_id
        self.store_id = store_id

    def __repr__(self):
        return '<User %r,%r>' % (self.user_id, self.store_id)
