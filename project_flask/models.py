from project_flask import db,login_manager,app
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
    
class User(db.Model,UserMixin):
   id = db.Column(db.Integer, primary_key = True)
   username = db.Column(db.String(120), unique=True, nullable=False)
   email = db.Column(db.String(120),  unique=True, nullable=False)
   image_file = db.Column(db.String(120), nullable=False , default='default.jpg')
   password = db.Column(db.String(120), nullable=False)
   date_created = db.Column(db.DateTime, default=datetime.utcnow)


   def get_token(self,expires_sec=30000):
        serial=Serializer(app.config['SECRET_KEY'],expires_sec)
        return serial.dumps({'user_id':self.id})


   @staticmethod
   def verify_token(token):
        serial=Serializer(app.config['SECRET_KEY'])
        try:
            user_id = serial.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    



   def __repr__(self):
        return f'User({self.username},{self.email},{self.password},{self.date_created.strftime("%d/%m/%Y, %H:%M:%S")}'
