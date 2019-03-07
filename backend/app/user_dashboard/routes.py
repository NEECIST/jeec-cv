from app import logger
from flask import jsonify, render_template, request, session, redirect, url_for, send_from_directory, current_app
from . import bp
from app.auth.wrappers import require_api_token
import os
from werkzeug.utils import secure_filename
from config import Config
import config
import json

from .handlers.file_handler import FileHandler

# content routes
@bp.route('/dashboard', methods=['GET'])
@require_api_token
def dashboard():
    filename = 'cv-' + session['username'] + '.pdf'

    if os.path.isfile(os.path.join(current_app.root_path, 'storage', filename)): 
        has_uploaded = True
    else:
        has_uploaded = False

    return render_template('user_dashboard.html', name=session['name'], username=session['username'], has_uploaded=has_uploaded)
    
# content routes
@bp.route('/dashboard', methods=['POST'])
@require_api_token
def dashboard_actions():
    if request.form['submit'] == 'Check':
        return redirect(url_for('user_dashboard.uploaded_file'))
    
    elif request.form['submit'] == 'Delete':
        return redirect(url_for('user_dashboard.delete_file'))
    
    elif request.form['submit'] == 'Upload':
        if 'file' not in request.files:
            logger.warning('Receiver upload request with no file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            logger.warning('User tried to upload empty file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = 'cv-' + session['username'] + '.pdf'

            FileHandler.upload_file(file, filename)
            logger.info('File uploaded sucessfuly!')
            
        return redirect(url_for('user_dashboard.dashboard'))


@bp.route('/delete', methods=['GET'])
@require_api_token
def delete_file():
    filename = 'cv-' + session['username'] + '.pdf'
    FileHandler.delete_file(filename)
    return redirect(url_for('user_dashboard.dashboard'))
    
@bp.route('/uploaded', methods=['GET'])
@require_api_token
def uploaded_file():
    filename = 'cv-' + session['username'] + '.pdf'
    return send_from_directory(os.path.join(current_app.root_path, 'storage'), filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

