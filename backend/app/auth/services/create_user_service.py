from app.models.user import User

class CreateUserService(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def call(self):
        user = User(**self.kwargs)

        user.create()
        user.reload()
        
        return user