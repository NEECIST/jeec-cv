import sqlalchemy
from app.models.company import Company

class CompanyFinder(object):

    @classmethod
    def get_from_username(cls, username):
        return Company.query.filter_by(username=username).first()