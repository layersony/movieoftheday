from sqlalchemy.orm import backref
from . import db
from datetime import datetime
from . import db,login_manager
from flask_login import current_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class Video:
  def __init__(self, key, name, type):
    self.key = key
    self.name = name
    self.type = type

class Horror:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

# Annimations
class Annimations:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

# Action
class Action:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

# Action
class Comedy:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

# Romance
class Romance:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class SciFi:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
# anime


# --------------------------------------SUBSCRIBERS-------------------------------------------------------------

class Subscriber(db.Model,UserMixin):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    movies = db.relationship("Movies", backref='subscribers',lazy='dynamic')
    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'

# ---------------------------------------------------------------------------------------------------


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin ,db.Model): # for creating new user
  __tablename__ = 'users' # allows us to give table in db a proper name

  id = db.Column(db.Integer, primary_key = True) # rep a single column 1st para type of data to be stored
  username = db.Column(db.String(255)) # db.String type of data to be stored is string (255) is max number
  email = db.Column(db.String(255), unique = True, index = True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  password_secure = db.Column(db.String(255))
#   reviews = db.relationship('Review', backref = 'user', lazy = 'dynamic')

  # to accessable to Users
  @property # used for the write only feature for the class property password for this property is not to be accessed by users
  def password(self): # this throws an error
    raise AttributeError('You cannot Read the password attribute')

  @password.setter
  def password(self, password):# password is hashed
    self.password_secure = generate_password_hash(password)

  def verify_password(self, password):# password_secure is checked if hashed
    return check_password_hash(self.password_secure, password)

  def __repr__(self):
    return f'User {self.username}' # not important just for debuging

class Popular(db.Model):
    __tablename__ = 'populars'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    overview = db.Column(db.Text(),nullable=False)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_popular_movie(id):
        popular = Popular.query.filter_by(id=id).first()

        return popular

    def __repr__(self):
        return f'Popular {self.title}'

class Genres:
    """
    """
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        

class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer,primary_key = True)
    movie_list = db.Column(db.String(255))
    subscriber = db.Column(db.Integer,db.ForeignKey("subscribers.id"))

    def save_movie_list(self):
        db.session.add(self)
        db.session.commit()

    # def __repr__(self):
    #     return f'Subscriber {self.email}'
