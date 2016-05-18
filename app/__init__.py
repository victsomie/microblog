from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#login configuration here
#---------
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
#--------------

#Flask-Login needs to know what view logs users in.
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'



app.config.from_object('config') #tell Flask to read it and use it
db = SQLAlchemy(app) #db is our databse

from app import views, models #adds a new import of a module called models


