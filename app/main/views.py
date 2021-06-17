from flask import render_template,redirect,url_for,abort,request,flash
from flask_sqlalchemy import SQLAlchemy
from . import main 
from .. import db, photos
from ..emails import mail_message
from app.models import Subscriber, Movies, User
from ..request import get_horror,get_action,get_animes,get_comedy,get_romance,get_scifi, get_movies, get_video, get_movie
from flask_login import login_required,current_user
from .forms import SimpleForm, UpdateProfile


# Views
@main.route('/')
def index():
  popular_movies = get_movies('popular')
  upcoming_movie = get_movies('upcoming')
  now_showing = get_movies('now_playing')

  heading = 'Working.. Good to go'
  return render_template('index.html', popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing)

@main.route('/movie/<int:id>')
def movie(id):

  movie = get_movie(id)
  yt_vid = get_video(id)
  title = f'{movie.title}'

  return render_template('movie.html', title = title, movie = movie, yt_vid=yt_vid)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404) # stops a request returns a response according to the status code indicated
  
  return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  return redirect(url_for('main.profile', uname=uname))

@main.route('/action')
def action():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Actions"
    sources = get_action()
    print(sources)
    return render_template('action.html',title=title, sources=sources)

@main.route('/anime')
def anime():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Anime"
    sources = get_animes()
    print(sources)
    return render_template('anime.html',title=title, sources=sources)

@main.route('/comedy')
def comedy():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Comedy"
    sources = get_comedy()
    print(sources)
    return render_template('comedy.html',title=title, sources=sources)

@main.route('/horror')
def horror():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Horror"
    sources = get_horror()
    print(sources)
    return render_template('horror.html',title=title, sources=sources)

@main.route('/romance')
def romance():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_romance()
    print(sources)
    return render_template('romance.html',title=title, sources=sources)

@main.route('/sci-fi')
def fiction():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_scifi()
    print(sources)
    return render_template('sci-fi.html',title=title, sources=sources)


# Saving Subscribers
@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
  
    check = Subscriber.query.filter_by(email = request.form.get('subscriber')).first()
    if check == request.form.get('subscriber'):
      return redirect(url_for('main.index'))
    else:
      email = request.form.get('subscriber')
      print(email)
      new_subscriber = Subscriber(email = email)
      new_subscriber.save_subscriber()
      # mail_message("Subscribed to Xtreme Movies","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
      flash('Successfuly subscribed')
      return redirect(url_for('main.choose_movie'))

@main.route('/subscribe/movies',methods = ['POST','GET'])
def choose_movie():
    form = SimpleForm()
    if form.validate_on_submit():
        data = form.example.data
        new_movie = Movies(movie_list= data)
        new_movie.save_movie_list()
        return redirect(url_for('main.index'))

    return render_template('subscribe.html',form = form)