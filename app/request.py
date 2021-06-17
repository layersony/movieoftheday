import urllib.request,json
from .models import Horror,Annimations,Action,Comedy,Romance, SciFi

# Getting the movie base url
# base_url = app.config["MOVIE_API_BASE_URL"]

# horror
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





