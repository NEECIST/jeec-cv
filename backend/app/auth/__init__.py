from flask import Blueprint, current_app
import os

bp = Blueprint('auth', __name__)

from .handlers.tecnico_client_handler import TecnicoClientHandler
fenix_config_file = 'fenixedu.ini'
client = TecnicoClientHandler.create_client(fenix_config_file=fenix_config_file)
    
from app.auth import routes