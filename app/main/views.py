from flask import render_template, redirect, url_for
from . import main
from ..request import get_movies, get_video, get_movie

@main.route('/')
def index():
  popular_movies = get_movies('popular')
  upcoming_movie = get_movies('upcoming')
  now_showing = get_movies('now_playing')


  return render_template('index.html', popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing)

@main.route('/movie/<int:id>')
def movie(id):

  movie = get_movie(id)
  yt_vid = get_video(id)
  title = f'{movie.title}'

  return render_template('movie.html', title = title, movie = movie, yt_vid=yt_vid)

