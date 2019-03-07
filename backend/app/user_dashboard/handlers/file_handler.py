import os
from app import logger
from werkzeug.utils import secure_filename
from flask import current_app, session


class FileHandler(object):

    @staticmethod
    def upload_file(file, filename):
        try:
            file.save(os.path.join(current_app.root_path, 'storage', filename))
            return True
        except Exception as e:
            logger.error(e)

    @staticmethod
    def delete_file(filename):
        try:
            os.remove(os.path.join(current_app.root_path, 'storage', filename))
        except Exception as e:
            logger.error(e)