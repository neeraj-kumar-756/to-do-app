from flask import Blueprint,request,redirect,url_for,render_template,flash,session
from app.models.forms import signupform
from app.models.model import User
from app import db
from sqlalchemy import or_

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('task.view_tasks'))
    if request.method == 'POST':
        username_or_email=request.form.get('username')
        password=request.form.get('password')

        user = User.query.filter(or_(User.username == username_or_email, User.email == username_or_email)).first()

        if user and user.check_password(password):
            session['user_id']=user.id
            flash("login succesfull",'success')
            return redirect(url_for('task.view_tasks'))
        else:
            flash("invalid username or password",'danger')
    return render_template('login.html')

@auth_bp.route("/logout")
def logout():
    session.pop('user_id',None)
    flash("logout successfully ",'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/signup',methods=['GET','POST'])
def signup():
    form = signupform()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {user.username}! Thank you for signing up. Please log in.",'success')
        return redirect(url_for('auth.login'))
    return render_template("signup.html",form=form)