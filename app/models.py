from datetime import datetime

from app import db
from flask import url_for

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    items = db.relationship('Item', backref='brand')

    def __repr__(self):
        return self.title


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    price = db.Column(db.Float(9, 2))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    logo = db.Column(db.String())
    users_items = db.relationship('UsersItem', backref='item', cascade='all,delete')

    def __repr__(self):
        return self.title

    @property
    def logo_url(self):
        return f'/static/{self.logo}' if self.logo else ''

    def get_update_url(self):
        return url_for('item_update', item_id=self.id)


    def get_absolute_url(self):
        return url_for('item_detail', item_id=self.id)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    users_items = db.relationship('UsersItem', backref='user', cascade='all,delete')

    def __repr__(self):
        return self.name


class UsersItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
