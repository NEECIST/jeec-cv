from app.models.student import Student
from app import logger

class CreateStudentService(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def call(self):
        logger.info("creating user")
        student = Student(**self.kwargs)
        

        student.create()
        student.reload()
        
        return student