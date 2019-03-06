from app import logger
from flask import jsonify, Response, request, redirect, session, url_for
from . import bp
import json

from .handlers.client_handler import ClientHandler

#student login
@bp.route('/login')
def login():
    url = ClientHandler.get_authentication_url()
    
    return redirect(url, code=302)

@bp.route('/redirect_uri')
def redirect_uri():
    fenix_auth_code = request.args.get('code')
    session['fenix_auth_code'] = fenix_auth_code
    
    user = ClientHandler.get_user(fenix_auth_code)
    person = ClientHandler.get_person(user)

    session['name'] = person['name']
    session['username'] = person['username']

    return redirect(url_for('user_dashboard.dashboard'))
    

@bp.route('/logout')
def logout():
   session.pop('fenix_auth_code', None)
   return redirect('/')

    # user = ClientHandler.get_user(code=code)
    # person = ClientHandler.get_person(user=user)

    # return person['name']
