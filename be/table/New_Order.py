from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class New_Order(db.Model):
    __tablename__ = 'new_order'
    order_id = db.Column(db.String(80), primary_key=True)
    user_id = db.Column(db.String(80), unique=True)
    store_id = db.Column(db.String(80), nullable=False)
