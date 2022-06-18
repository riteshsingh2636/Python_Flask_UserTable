from project_flask import app,db,bcrypt,mail
from flask import flash, render_template,redirect, url_for
from project_flask.forms import Registrationform,Loginform,ResetRequestform,ResetPasswordform
from project_flask.models import User
from flask_login import login_user,logout_user,current_user
from flask_mail import Message
 
@app.route("/")
@app.route("/home")
def homepage():
    return render_template("layout.html", title='Home')


@app.route("/register",methods=['POST','GET'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        encrypted_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}','success')
        return redirect (url_for('login'))
    return render_template("register.html",title='Sing Up',form=form)



@app.route("/login",methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))


    form = Loginform()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f'Login successfully for {form.email.data}',category='success')

            return redirect(url_for('account'))
        else:
            flash(f'Login unsuccessfully for {form.email.data}',category='danger')
    return render_template("login.html",title='Login',form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


def send_mail(user):
    token=user.get_token('self')
    msg=Message('password Reset Request',recipients=[user.email],sender='ritesh123shivam@gmail.com')
    msg.body=f'''To reset your password.

    {url_for('reset_token', token=token,_external=True)}
    If you didn't send a password reset request. Please ignore this message.
    
    
    '''
    mail.send(msg)



@app.route("/reset_password",methods=['POST','GET'])
def reset_request():
    form = ResetRequestform()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            send_mail(user)
            flash('Reset request sent. Check your mail.','success')
            return redirect (url_for('login'))

    return render_template("reset_request.html", title='Reset Request',form=form, legend='Reset Password')


@app.route('/reset_password/<token>',methods=['GET','POST'])
def reset_token(token):
    User.verify_token(token)
    if User is None :
        flash('that is invalid token or expired.please try again','warning')
        return redirect (url_for('reset_request'))

    form=ResetPasswordform()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        User.password=hashed_password

        db.session.commit()
        flash('Password changed successfully','success')
        return redirect(url_for('login'))
    return render_template("change_password.html",title='Change password',legend='Change password',form=form)





@app.route("/account")
def account():
    return render_template("account.html", title='Account')