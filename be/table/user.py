
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class user(db.model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.Text, nullable=True)
    balance = db.Columns(db.Integer, nullable=True)
    token = db.Columns(db.Text)
    terminal = db.Columns(db.Text)
