from flask import current_app
from app import logger
from app.auth import client


class ClientHandler(object):

    @staticmethod
    def get_authentication_url():
        url = client.get_authentication_url()
        return url

    @staticmethod
    def get_user(code):
        user = client.get_user_by_code(code)
        return user

    @staticmethod
    def get_person(user):
        person = client.get_person(user)
        return person