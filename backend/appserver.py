from app import create_app
from app.database import db
from app.models.company import Company
from app.models.user import User

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", ssl_context='adhoc')