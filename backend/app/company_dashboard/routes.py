from app import logger
from flask import jsonify, send_file, Response, render_template, request, session, redirect, url_for, send_from_directory, current_app
from . import bp
import os
from werkzeug.utils import secure_filename
from config import Config
import config
import json
from flask_login import login_required
from .handlers.file_handler import FileHandler


# content routes
@bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    logger.info('entered dashboard!')
    company_name = session['name']
    company_logo = '/static/partner-logos/' + company_name.lower() + '.png'
    return render_template('company_dashboard.html', name=company_name, logo=company_logo)
        
# content routes
@bp.route('/dashboard', methods=['POST'])
@login_required
def dashboard_actions():
    if request.form['submit'] == 'Download Files':
        zip_file = FileHandler.get_files_zip()
        
        if not zip_file:
            return Response(response="Invalid zip file", status="400")

        return send_file(
            zip_file,
            as_attachment=True,
            attachment_filename='curriculos_JEEC19.zip')

    return redirect(url_for('company_dashboard.dashboard'))