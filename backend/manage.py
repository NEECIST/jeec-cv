from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from appserver import app
from app.database import db
import os, os.path

def count_files():
    current_path = os.path.dirname(os.path.realpath(__file__))
    directory =  os.path.join(current_path, 'app', 'storage')
    print('Number of files in storage: ' + str(len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])))
    exit()

manager = Manager(app)

current_path = os.path.dirname(os.path.realpath(__file__))

migrations_dir = os.path.join(current_path, 'app', 'database', 'migrations')
migrate = Migrate(app, db, directory=migrations_dir)

manager.add_command('db', MigrateCommand)

manager.add_command('cv_count', count_files())

if __name__ == '__main__':
    manager.run()