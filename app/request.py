import urllib.request, json
from .models import Movie, Video

api_key = None
base_url = None 
vid_url = None

def configure_request(app):
  global api_key, base_url, vid_url
  api_key = app.config['MOVIE_API']
  base_url = app.config['BASE_URL']
  vid_url = app.config['VID_URL']

def get_movies(category):
  main_url = base_url.format(category, api_key)
  with urllib.request.urlopen(main_url) as url:
    data = url.read()
    json_data = json.loads(data)

    movie_list = None

    if json_data['results']:
      data_list = json_data['results']
      movie_list = process_results(data_list)
    
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
  
def process_results(movieList):

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
  