# Pour le, vous aurez des itinéraires pour récupérer à la fois la page de connexion () et la page d’inscription (). Enfin, vous disposerez d’une route de déconnexion () pour déconnecter un utilisateur actif.auth_blueprint/login/signup/logout

# Ensuite, créez :auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required , logout_user
# from flask_bootstrap import Bootstrap
from .models import User
from . import db

auth = Blueprint('auth', __name__)

# @auth.route('/login')
# def login():
#     return 'Login'

# @auth.route('/signup')
# def signup():
#     return 'Signup'

# ================= dash board
@auth.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ================== signup
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add to database goes here7
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. hash the password so plaintext version isn't saved
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

# ===========login
@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post(): 
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take if the user-supplied password, hash it, and compare it to the hashed password in
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))
    
# ============ logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
