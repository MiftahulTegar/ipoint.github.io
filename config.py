from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import *
import os

class Config(object):
    SECRET_KEY = 'my-secrete-key'

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config["SECRET_KEY"] = "konstruksisoftwarecourse"
app.permanent_session_lifetime = timedelta(hours=3)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:@localhost/KPL"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



