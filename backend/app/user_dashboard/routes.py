from app import logger
from flask import jsonify, Response, request, session, redirect, url_for
from . import bp
from app.auth.wrappers import require_api_token
import os
from werkzeug.utils import secure_filename
from config import Config
import json

# content routes
@bp.route('/dashboard')
@require_api_token
def dashboard():
    
    return jsonify({'welcome message': "Hi, this is the file dashboard" + session['name']})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #file.save(os.path.join(Config.U, filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@bp.route('/handlefile', methods=['POST'])
def add_file():
    return jsonify({'welcome message': "Hi, this is JEEC CV Platform"})

    
@bp.route('/get', methods=['GET'])
def get_file():
    return jsonify({'welcome message': "Hi, this is JEEC CV Platform"})

