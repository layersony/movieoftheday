from . import db
from datetime import datetime
from . import db,login_manager
from flask_login import current_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class Movies:
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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User (UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email = db.Column(db.String(255), unique = True,nullable = False)
    bio = db.Column(db.String(255),default ='My default Bio')
    profile_pic_path = db.Column(db.String(150),default ='default.png')
    hashed_password = db.Column(db.String(255),nullable = False)
    popular = db.relationship('Popular', backref='user', lazy='dynamic')
    
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "User: %s" %str(self.username)

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
class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'


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

    def __init__(self,id,title,overview,poster,vote_average,vote_count,genres):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/ + poster"
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

