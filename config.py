import os
import secrets

secret =secrets.token_urlsafe(32)

class Config:
  SECRET_KEY = secret
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
  VID_URL = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}'
  MOVIE_API = 'a72cf63dfc93d3aa208d591b54dd2c81'

class ProdConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = ''
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}