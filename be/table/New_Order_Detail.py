from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  ForeignKey
db = SQLAlchemy()

class new_order_detail(db.model):
    __tablename__ = 'new_order_detail'
    order_id = db.Column(db.String(80), primary_key=True)
    book_id = db.Column(db.String(80), ForeignKey('book.book_id'))
    count = db.Column(db.Integer(), nullable=False)
    price=db.Column(db.Integer(), nullable=False)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class New_Order_Detail(db.Model):
    __tablename__ = 'new_order_detail'
    order_id = db.Column(db.String(80), primary_key=True)
    book_id = db.Column(db.String(80), primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
