from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_client = FlaskRedis(app)
migrate = Migrate(app, db)

from main_page import main
from mod_admin import admin
from mod_users import users

app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(users)
