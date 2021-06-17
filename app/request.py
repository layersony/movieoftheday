import urllib.request, json
from .models import Horror,Annimations,Action,Comedy,Romance, SciFi, Genres,Movie, Video, Genres


api_key = None
base_url = None
base_horror_url = None
api_key = None
vid_url = None


def configure_request(app):
    global api_key,base_url, base_horror_url, api_key, vid_url
    base_url = app.config['MOVIE_API_MOVIE_BASE_URL']
    base_horror_url = app.config['HORROR_GENRE_URL']
    api_key = app.config['MOVIE_API']
    vid_url = app.config['VID_URL']


def get_movies(category):
  main_url = base_url.format(category, api_key)
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
      movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
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
  
def get_horror():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = "https://api.themoviedb.org/3/discover/movie?api_key=68b935daae11d4366ca1ccbb3944bce2&with_genres=18"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

def process_results(movie_list):
   
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Horror(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

# Annimations
def get_animes():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = "https://api.themoviedb.org/3/discover/movie?api_key=68b935daae11d4366ca1ccbb3944bce2&with_genres=16"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Annimations(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

# Action
def get_action():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = "https://api.themoviedb.org/3/discover/movie?api_key=68b935daae11d4366ca1ccbb3944bce2&with_genres=28"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Action(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

# Comedy
def get_comedy():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = "https://api.themoviedb.org/3/discover/movie?api_key=68b935daae11d4366ca1ccbb3944bce2&with_genres=35"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Comedy(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

# Romance
def get_romance():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = "https://api.themoviedb.org/3/discover/movie?api_key=68b935daae11d4366ca1ccbb3944bce2&with_genres=10749"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Romance(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results


# scifi
def get_scifi():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = "https://api.themoviedb.org/3/discover/movie?api_key=68b935daae11d4366ca1ccbb3944bce2&with_genres=878"

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = SciFi(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results





