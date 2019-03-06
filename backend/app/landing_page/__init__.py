from flask import Blueprint

bp = Blueprint('landing_page', __name__)

from app.landing_page import routes