from app.database import db
from app.database.model import ModelMixin
import sqlalchemy
import uuid


class Company(ModelMixin, db.Model):
    __tablename__ = 'company'
    
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    password = db.Column(db.String(100))

    remember_token = db.Column(db.String(100))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<email:: {}  |  Name: {}>'.format(self.email, self.name)