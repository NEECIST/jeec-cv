from app.database import db
from app.database.model import ModelMixin
import sqlalchemy
import uuid


class User(ModelMixin, db.Model):
    __tablename__ = 'contact'
    
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    password = db.Column(db.String(100))

    course = db.Column(db.String(100))

    remember_token = db.Column(db.String(100))

    istid = db.Column(db.String(10))
    
    def __init__(self, name, istid, email, course):
        self.name = name
        self.istid = istid
        self.email = email
        self.course = course

    def __repr__(self):
        return '<email:: {}  |  Name: {}>'.format(self.email, self.name)