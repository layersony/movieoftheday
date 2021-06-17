from flask import render_template,redirect,url_for,abort,request,flash
from . import main
from ..emails import mail_message
from ..request import get_horror,get_action,get_animes,get_comedy,get_romance,get_scifi

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to Xtreme Movies'
    return render_template('index.html',title=title)

# Action
@main.route('/action')
def action():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_horror()
    print(sources)
    return render_template('action.html',title=title, sources=sources)


# Animation
@main.route('/anime')
def anime():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_animes()
    print(sources)
    return render_template('anime.html',title=title, sources=sources)


# comedy
@main.route('/comedy')
def comedy():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_comedy()
    print(sources)
    return render_template('comedy.html',title=title, sources=sources)


# Horror
@main.route('/horror')
def horror():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_horror()
    print(sources)
    return render_template('horror.html',title=title, sources=sources)


# Romance
@main.route('/romance')
def romance():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_romance()
    print(sources)
    return render_template('romance.html',title=title, sources=sources)

#Sci-Fi
@main.route('/sci-fi')
def fiction():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Global News"
    sources = get_scifi()
    print(sources)
    return render_template('sci-fi.html',title=title, sources=sources)
