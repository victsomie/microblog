from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #tell Flask to read it and use it


from app import views
