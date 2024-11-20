from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)



app.config['SECRET_KEY']="thisisfirstflaskapp"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/pjflask.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='ritesh123shivam@gmail.com'          # enter your email
app.config['MAIL_PASSWORD']='obwvuwynsbyomghl'          #enter your password 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)

from project_flask import routes


