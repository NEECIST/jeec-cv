import zipfile
import os
import io
from flask import current_app
from app import logger


class CompressFilesService(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def call(self):
        directory =  os.path.join(current_app.root_path, 'storage')
        contents = os.walk(directory)  

        memory_file = io.BytesIO()

        zip_file = zipfile.ZipFile(memory_file, 'w')
        
        for root, dirs, files in contents:
            for file in files:
                zip_file.write(os.path.join(root, file))

        test_zip = zip_file.testzip()

        if test_zip is not None:
            logger.info('Zip file is corrupt!') 
            return None

        size = sum([zinfo.file_size for zinfo in  zip_file.filelist])
        zip_kb = float(size)/1000 #kB       
        logger.info('Size of the zip: ' + str(zip_kb))

        logger.info("Zip file created!")
        memory_file.seek(0)
        return memory_file
        
        