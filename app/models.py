from . import db
from datetime import datetime
class Movie:
  def __init__(self,id,title,overview,poster,vote_average,vote_count):
    self.id =id
    self.title = title
    self.overview = overview
    self.poster = 'https://image.tmdb.org/t/p/w500'+ poster
    self.vote_average = vote_average
    self.vote_count = vote_count

class Video:
  def __init__(self, key, name, type):
    self.key = key
    self.name = name
    self.type = type
