from flask import session
from app import logger
from app.auth.services.create_user_service import CreateUserService
from app.auth.finders.user_finder import UserFinder

class AuthHandler(object):

    @staticmethod
    def check_for_user():
        user = UserFinder.get_from_istid(session['username'])

        if user is None:
            try:
                CreateUserService(username=session['username']).call()
                session['first_time_login'] = True
                return False
            except Exception as e:
                logger.error(e)
        else:
            if user.acceptedTerms == False:
                session['first_time_login'] = True
            else:
                session['first_time_login'] = False
            return True