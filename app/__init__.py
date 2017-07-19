from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config.from_object('app.settings')

db = SQLAlchemy(app)
CSRFProtect(app)
mograte = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from .views import core_pages
from users.views import user_pages

from users.models import *

app.register_blueprint(core_pages)
app.register_blueprint(user_pages)