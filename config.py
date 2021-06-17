import os
import secrets

secret =secrets.token_urlsafe(32)

class Config:
  # MOVIES_BASE_URL =
  MOVIE_API_BASE_URL ="https://api.themoviedb.org/3/genre/tv/list?api_key={}&language=en-US"
  MOVIE_API_KEY = "68b935daae11d4366ca1ccbb3944bce2"
  MOVIE_API_MOVIE_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
  HORROR_GENRE_URL = 'https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres=27'


  SECRET_KEY = secret
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = ''
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}