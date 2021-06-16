from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
boostrap = Bootstrap()
def create_app(config_name):
  app = Flask(__name__)

  app.config.from_object(config_options[config_name])

  db.init_app(app)
  boostrap.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix= '/authenticate')

  from .request import configure_request
  configure_request(app)
  return app
  