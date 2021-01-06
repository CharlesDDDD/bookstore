from sqlalchemy import Column, Integer, String, Text
from be.model.database import Base


class User(Base):
    __tablename__ = 'user'
    user_id = Column(String(120), primary_key=True)
    password = Column(String(120), nullable=True)
    balance = Column(Integer, nullable=True)
    token = Column(Text)
    terminal = Column(Text)

    def __init__(self, user_id=None, password=None, balance=None, token=None, terminal=None):
        self.user_id = user_id
        self.password = password
        self.balance = balance
        self.token = token
        self.terminal = terminal

    def __repr__(self):
        return '<User %r,%r,%r,%r,%r>' % (self.name,self.password,self.balance,self.terminal,self.terminal)
