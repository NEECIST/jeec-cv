from app import logger
from flask import jsonify, Response, request, redirect, session, url_for
from . import bp
import json


@bp.route('/')
def index():
    
    return redirect('www.google.com', code=302)


