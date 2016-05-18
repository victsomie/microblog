from flask import render_template, flash, redirect, session, url_for, request, g #Added imports
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .form import LoginForm
from .models import User #imported our LoginForm class, instantiated an object from it




@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('hello.html',
                           title='Index',
                           user=user,
                           posts=posts)

@app.route('/hello')
def hello():
    #user = {'nickname': 'Peter'}  # fake user
    user = g.user #This ensures that it is accessible to only logged in users
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Victor 2'},
            'body': 'It\' cool learning Flask!'
        },
        {
            'author': {'nickname': 'Victor 2'},
            'body': 'another thing her!'
        }
    ]
    return render_template('hello.html',
                           title='Page ingine ya hello!',
                           user=user,
                           posts=posts)
@app.before_request
def before_request():
    g.user = current_user

@app.route('/about')
def about():
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



"""
def jlogin():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

"""
@app.route('/login', methods=['GET', 'POST'])
#methods argument in the route decorator. This tells Flask that this view function accepts GET and POST requests
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


#function that loads a user from the database
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
"""
Note how this function is registered with Flask-Login through the lm.user_loader decorator. Also remember that user ids in Flask-Login are always unicode strings, so a conversion to an integer is necessary before we can send the id to Flask-SQLAlchemy.

"""

#after_login function below
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))
