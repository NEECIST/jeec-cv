import os
from app import logger
from flask import current_app, session
from app.company_dashboard.services.compress_files_service import CompressFilesService

class FileHandler(object):

    @staticmethod
    def get_files_zip():
        try:
            zip_file = CompressFilesService().call()
            return zip_file
        except Exception as e:
            logger.error(e)
            return None


