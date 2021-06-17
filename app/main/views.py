from flask import render_template,redirect,url_for,abort,request,flash
from . import main
from ..emails import mail_message
from app.models import Popular,Subscriber,User,Review
from ..request import get_genres,get_annimation, get_movies, get_video, get_movie

# home route
@main.route('/')
def index():

  popular_movies = get_movies('popular')
  upcoming_movie = get_movies('upcoming')
  now_showing = get_movies('now_playing')

  name = get_genres("name")
  id = get_genres("id")
  # genres = get_genres("name")

  heading = 'Working.. Good to go'
  return render_template('index.html',  name=name, id=id, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing)

@main.route('/movie/<int:id>')
def movie(id):

  movie = get_movie(id)
  yt_vid = get_video(id)
  title = f'{movie.title}'

  return render_template('movie.html', title = title, movie = movie, yt_vid=yt_vid)

@main.route('/animation')
def animation():
  name = get_annimation()

  return render_template('anime.html',name=name)

# subscribers
@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Popular movies","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))
