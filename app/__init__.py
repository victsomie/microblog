from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#login configuration here
#---------
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir



lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
#--------------



app = Flask(__name__)
app.config.from_object('config') #tell Flask to read it and use it
db = SQLAlchemy(app) #db is our databse

from app import views, models #adds a new import of a module called models


