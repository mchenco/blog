from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

                          ##### for index page #####
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
#calls render_template fxn flask, tells what html file to pull from, the title of the page, and the content shown 

                          ##### for login form #####

@app.route('/login', methods=['GET', 'POST'])
#has both GET and POST functions

def login():
    form = LoginForm() #calls imported LoginForm constructor
    if form.validate_on_submit(): #returns T if data is valid
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
                            



