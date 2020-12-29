from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class store(db.model):
    __tablename__ = 'store'
    store_id = db.Column(db.String(80), primary_key=True)
    book_id = db.Column(db.String(80), primary_key=True)
    book_info = db.Column(db.String(80), nullable=True)
    stock_level = db.Column(db.Integer, nullable=True)
