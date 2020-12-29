from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class new_order_detail(db.model):
    __tablename__ = 'new_order_detail'
    order_id = db.Column(db.String(80), primary_key=True)
    book_id = db.Column(db.String(80), primary_key=True)
    count = db.Column(db.Interger, nullable=False)
    price = db.Column(db.Interger, nullable=False)
