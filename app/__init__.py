from flask import Flask
fform flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #tell Flask to read it and use it
db = SQLAlchemy(app)

from app import views, models
