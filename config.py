WTF_CSRF_ENABLED = True #activates the cross-site request forgery prevention
SECRET_KEY = 'you-will-never-guess' #create a cryptographic token that is used to validate a form. NB: This is only needed when CSRF is enabled

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')#required by the Flask-SQLAlchemy extension. This is the path of our database file.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#SQLALCHEMY_MIGRATE_REPO is the folder where we will store the SQLAlchemy-migrate data files
