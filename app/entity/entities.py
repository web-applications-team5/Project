import datetime

from app.entity import db
from app.entity.Serializer import Serializer


class Address(db.Model, Serializer):
    __tablename__ = 'address'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    addressLine = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)


class Restaurant(db.Model, Serializer):
    __tablename__ = 'restaurant'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    openTime = db.Column(db.Time, nullable=False)
    closeTime = db.Column(db.Time, nullable=False)
    logo = db.Column(db.String(255))
    description = db.Column(db.String(5000))
    rating = db.Column(db.INTEGER)
    address_id = db.Column(db.ForeignKey(u'address.id'), nullable=False, index=True)

    address = db.relationship(u'Address')


class Menu(db.Model, Serializer):
    __tablename__ = 'menu'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    restaurant_id = db.Column(db.ForeignKey(u'restaurant.id'), nullable=False, index=True)

    restaurant = db.relationship(u'Restaurant')


class Photo(db.Model, Serializer):
    __tablename__ = 'photo'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    url = db.Column(db.String(1024), nullable=False)
    restaurant_id = db.Column(db.ForeignKey(u'restaurant.id'), nullable=False, index=True)

    restaurant = db.relationship(u'Restaurant')


class OrderUser(db.Model, Serializer):
    __tablename__ = 'user'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(12))
    email = db.Column(db.String(255))


class MenuItem(db.Model, Serializer):
    __tablename__ = 'menuItem'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(5000))
    photo = db.Column(db.String(1024))
    status = db.Column(db.String(45), nullable=False)
    menu_id = db.Column(db.ForeignKey(u'menu.id'), nullable=False, index=True)

    menu = db.relationship(u'Menu')


class Order(db.Model, Serializer):
    __tablename__ = 'order'

    status = 'ACTIVE'
    createdDate = datetime.datetime

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    status = db.Column(db.String(10))
    confirmationNumber = db.Column(db.String(100))
    createdDate = db.Column(db.String(45))
    user_id = db.Column(db.ForeignKey(u'user.id'), nullable=False, index=True)

    user = db.relationship(u'OrderUser')


class OrderItem(db.Model, Serializer):
    __tablename__ = 'orderItem'

    id = db.Column(db.INTEGER, primary_key=True, unique=True, autoincrement=True)
    quantity = db.Column(db.INTEGER)
    order_id = db.Column(db.ForeignKey(u'order.id'), nullable=False, index=True)
    menuItem_id = db.Column(db.ForeignKey(u'menuItem.id'), nullable=False, index=True)

    menuItem = db.relationship(u'MenuItem')
    order = db.relationship(u'Order')