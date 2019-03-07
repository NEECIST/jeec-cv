import sqlalchemy
from app.models.user import User

class UserFinder(object):

    @classmethod
    def get_from_istid(cls, istid):
        return User.query.filter_by(istid=istid)