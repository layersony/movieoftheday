import urllib.request, json
from .models import Movies, Video, Genres
import urllib.request,json
from .models import Genres,Movie

api_key = None
base_url = None
base_horror_url = None
main_api_key = None
main_base_url = None 
vid_url = None


def configure_request(app):
    global api_key,base_url, base_horror_url, main_api_key, main_base_url, vid_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    base_horror_url = app.config['HORROR_GENRE_URL']
    main_api_key = app.config['MOVIE_API']
    main_base_url = app.config['BASE_URL']
    vid_url = app.config['VID_URL']


def get_movies(category):
  main_url = base_url.format(category, main_api_key)
  with urllib.request.urlopen(main_url) as url:
    data = url.read()
    json_data = json.loads(data)

    movie_list = None

    if json_data['results']:
      data_list = json_data['results']
      movie_list = process_result(data_list)
    
    return movie_list

def get_video(movie_id):
  main_vid_url = vid_url.format(movie_id, api_key)
  with urllib.request.urlopen(main_vid_url) as url:
    vid_data = url.read()
    vid_json_data = json.loads(vid_data)

    trailerlink = None

    if vid_json_data['results']:
      vid_list = vid_json_data['results']
      trailerlink = processvid(vid_list)

    return trailerlink
  
def get_movie(id):
  main_url = base_url.format(id, api_key)

  with urllib.request.urlopen(main_url) as url:
    movie_details_data = url.read()
    movie_details_response = json.loads(movie_details_data)

    movie_object = None

    if movie_details_response:
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')
        vote_average = movie_details_response.get('vote_average')
        vote_count = movie_details_response.get('vote_count')

        movie_object = Movie(id, title, overview, poster, vote_average, vote_count)

  return movie_object
  
def process_result(movieList):

  processedList= []

  for movie_item in movieList:
    id = movie_item.get('id')
    title = movie_item.get('title')
    overview = movie_item.get('overview')
    poster = movie_item.get('poster_path')
    vote_average = movie_item.get('vote_average')
    vote_count = movie_item.get('vote_count')

    if poster:
      movie_object = Movies(id, title, overview, poster, vote_average, vote_count)
      processedList.append(movie_object)

  return processedList

def processvid(movielinks):
  trailer = None

  for item in movielinks:
    if item.get('type') == 'Trailer':
      key = item.get('key')
      name = item.get('name')
      type = item.get('type')

      trailer = Video(key, name, type)
  
  return trailer
  

def get_genres(name):
    """
    """
    get_genres_url = base_url.format(api_key)

    with urllib.request.urlopen(get_genres_url) as url:
        get_genres_data = url.read()
        get_genres_response = json.loads(get_genres_data)

        genre_results = None

        if get_genres_response['genres']:
            genres_results_list = get_genres_response['genres']
            genre_results = process_results(genres_results_list)

    return genre_results

def process_results(genre_list):
    genre_results = []

    for item in genre_list:
        id = item.get('id')
        name = item.get('name')

        if id:
            genre_object = Genres(id, name)
            genre_results.append(genre_object)

    return genre_results

def get_horrors():
    horror = base_horror_url.format(api_key)
    with urllib.request.urlopen(horror) as url:
        horror_data = url.read()
        horror_response = json.loads(horror_data)
    return horror_response
    
# Annimation
def get_annimation():
    sources ='https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres=16'.format(api_key)

    
    with urllib.request.urlopen(sources) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['genre_id']:
            movie_results_list = get_movies_response['genre_id']
            movie_results = process_results(movie_results_list)


    return movie_results

def process_results(movie_list):
    movie_results = []
    for genre in movie_list:
        id = genre.get("id")
        name = genre.get("name")
        overview = genre.get('overview')
        poster = genre.get('poster_path')
        vote_average = genre.get('vote_average')
        vote_count = genre.get('vote_count')
        genres = genre.get('genres')

        if name:
            movie_object = Movie(id,name,overview,poster,vote_average,vote_count,genres)
            movie_results.append(movie_object)      
    return movie_results

