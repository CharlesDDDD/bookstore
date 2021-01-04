
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.Text, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    token = db.Column(db.Text)
    terminal = db.Column(db.Text)
