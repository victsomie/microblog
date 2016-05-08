from flask import render_template, flash, redirect #Added imports
from app import app
from .form import LoginForm  #imported our LoginForm class, instantiated an object from it




@app.route('/')
@app.route('/index')

@app.route('/hello')
def hello():
    user = {'nickname': 'Peter'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Victor 2'},
            'body': 'It\' cool learning Flask!'
        }
    ]
    return render_template('hello.html',
                           title='Page ingine ya hello!',
                           user=user,
                           posts=posts)


@app.route('/about')
def index():
    user = {'nickname': 'Peter'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': {'nickname': 'victor'}, 
            'body': 'Python is cool too!' 
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)



def jlogin():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
#methods argument in the route decorator. This tells Flask that this view function accepts GET and POST requests
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
