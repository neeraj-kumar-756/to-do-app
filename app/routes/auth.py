from flask import Blueprint,request,redirect,url_for,render_template,flash,session

auth_bp = Blueprint('auth',__name__)

USER_CREDETIONAL = {
    "username":"admin",
    "password":"12345"
}

@auth_bp.route('/login',method=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username == USER_CREDETIONAL['username'] and password == USER_CREDETIONAL['password']:            
            session['user']=username
            flash("login succesfull",'success')
        else:
            flash("invalid username or password",'danger')
    return render_template('login.html')

@auth_bp.route("/logout")
def logout():
    session.pop('user',None)
    flash("logout successfully ",'info')
    return redirect(url_for('auth.login'))
