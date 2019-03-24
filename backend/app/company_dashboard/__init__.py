from flask import Blueprint

bp = Blueprint('company_dashboard', __name__)

from app.company_dashboard import routes
