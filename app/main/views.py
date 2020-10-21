from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_news1,search_news,get_sources
from ..models import Review

# Views
@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    sources= get_sources()
    title = 'Welcome to the News website'
    search_news1 = request.args.get('news1_query')

    if search_news1:
        return redirect(url_for('search',news1_name=search_news1))
    else:
        return render_template('index.html', title = title,  sources = sources)

@main.route('/articles/<string:source_id>')
def source(source_id):
    articles = get_news(source_id)
    return render_template('news.html', articles = articles)
    

    
@main.route('/news/<int:id>')
def movie(id):

    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)


@main.route('/search/<news1_name>')
def search(news1_name):
    '''
    View function to display the search results
    '''
    news1_name_list = news1_name.split(" ")
    news1_name_format = "+".join(news1_name_list)
    searched_news = search_news(news1_name_format)
    title = f'search results for {news1_name}'
    return render_template('search.html',news = searched_news)