from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Drake'} #fake user
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'Kanye'},
            'body': 'I miss the old Kanye, straight from the go Kanye'
        },
        {
            'author': {'nickname': 'Migos'},
            'body': 'Hit em with the left, hit em with the right'
        }
    ]
    return render_template('index.html',title = 'Home', user=user, posts=posts)
