from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.db'
app.config['SECRET_KEY'] = 'thisisserects'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(120), unique=True, nullable=False)
   phone = db.Column(db.String(120), nullable=False) 
   address = db.Column(db.String(120), nullable=False)
   email = db.Column(db.String(120),  unique=True, nullable=False)



   def __repr__(self):
       return f"User('{self.name}','{self.phone}','{self.address}','{self.email}')"




@app.route('/')
def index():
    all_data= User.query.all()
    return render_template('main.html',users=all_data)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=='POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        email = request.form.get('email')
        user = User(name=name,phone=phone,address=address,email=email)
        db.session.add(user)
        db.session.commit()
        flash('user has been added successfully','success')
        return redirect('/')
    return render_template("add.html")





@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    all_data= User.query.get(id)
    if request.method=='POST':
        all_data.name=request.form.get('name')
        all_data.phone=request.form.get('phone')
        all_data.address=request.form.get('address')
        all_data.email=request.form.get('email')
        db.session.commit()
        flash("Post has been updated",'success')
        return redirect('/')
    return render_template('update.html',users=all_data)



@app.route("/delete/<int:id>",methods=['GET','POST'])
def delete_post(id):
    all_data = User.query.get(id)
    db.session.delete(all_data)
    db.session.commit()
    flash("Post has been deleted",'success')
    return redirect('/')



if __name__ == "__main__":
    app.secret_key= "012#!ApaAjaBoleh)(*^%"
    app.run(debug=True)