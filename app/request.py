import urllib.request,json
from .models import Genres,Movie

# Getting api key
api_key = None
# Getting the movie base url for genres
base_url = None
# get movie movie ur for movies
base_horror_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    base_horror_url = app.config['HORROR_GENRE_URL']
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

