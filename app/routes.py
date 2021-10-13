from app import app
from flask import render_template 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favorite')
def favorites():
    my_favorites = ['Lyon', 'New York', 'New Orleans', 'London', 'Quebec City']
    title = 'Favorites Page'
    return render_template('favorite.html', title = title, favorites = my_favorites)