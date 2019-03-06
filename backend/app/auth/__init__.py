from flask import Blueprint
import fenixedu

bp = Blueprint('auth', __name__)

fenix_config_file = 'fenixedu.ini'
config = fenixedu.FenixEduConfiguration.fromConfigFile(fenix_config_file)

client = fenixedu.FenixEduClient(config)

from app.auth import routes