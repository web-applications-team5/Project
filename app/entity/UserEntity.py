from app.entity import db
from app.entity.Serializer import Serializer


class user(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return Serializer.serialize(self)

    def serializeAll(users):

        serialized_users = []
        for usr in users :
            serialized_users.append(usr.serialize())

        return serialized_users;