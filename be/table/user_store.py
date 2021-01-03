
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class user_store(db.model):
    __tablename__ = 'user_store'
    user_id = db.Column(db.String(80), primary_key=True)
    store_id = db.Column(db.String(80), primary_key=True)
