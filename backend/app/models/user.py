from app.database import db
from app.database.model import ModelMixin
import sqlalchemy
import uuid


class User(ModelMixin, db.Model):
    __tablename__ = 'user'
    
    name = db.Column(db.String(100))
    istid = db.Column(db.String(10), unique=True)

    acceptedTerms = db.Column(db.Boolean, default=False)

    
    def __init__(self, name, istid, email, course):
        self.name = name
        self.istid = istid

    def __repr__(self):
        return '<email:: {}  |  Name: {}>'.format(self.email, self.name)