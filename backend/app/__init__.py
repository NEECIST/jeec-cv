from flask import Flask
from config import config, Config
from flask_migrate import Migrate
from flask_cors import CORS
from app.database import db, create_tables
import logging
import os

def initialize_landing_page_api_blueprint(app):
    from app.landing_page import bp as landing_page_bp
    app.register_blueprint(landing_page_bp)

def initialize_user_dashboard_api_blueprint(app):
    from app.user_dashboard import bp as user_dashboard_bp
    app.register_blueprint(user_dashboard_bp, url_prefix='/user')

def initialize_auth_api_blueprint(app):
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

def initialize_admin_api_blueprint(app):
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')


def create_app():
    app = Flask(__name__)

    env_config = Config.APP_ENV
    app.config.from_object(config[env_config])

    current_path = os.path.dirname(os.path.realpath(__file__))

    migrations_dir = os.path.join(current_path, 'database', 'migrations')
    Migrate(app, db, directory=migrations_dir)
    
    with app.app_context():
        db.init_app(app)
        create_tables()

    CORS(app) # enable Cross-Origin Resource Sharing


    initialize_user_dashboard_api_blueprint(app)
    initialize_auth_api_blueprint(app)
    initialize_admin_api_blueprint(app)
    
    return app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)