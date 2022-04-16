from datetime import datetime

from app import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    items = db.relationship('Item', backref='brand', cascade='all,delete')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    price = db.Column(db.Numeric(9, 2))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
