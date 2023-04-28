from flask import Blueprint, render_template ,  request, flash, redirect, url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                #flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('dashboard.home'))
            else:
                flash('Incorrect password, Please try again.', category='errors')
        else:
            flash('Email does not exist.Please Signup', category='errors')
            return redirect(url_for('auth.sign_up'))
    return render_template("login.html", user=current_user)





@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        company_name = request.form.get('company_name')
        Full_Name = request.form.get('Full_Name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if len(Full_Name) <2:
            flash('Full name must be greater than 3 charcters' ,category='errors')
        elif len(phone_number)<10:
            flash('Enter the 10 digit phone number without country code', category='errors')
        elif len(password)<6:
            flash('Enter the password greater than 6 characters', category='errors')
        elif password != confirm_password:
            flash('Passwords are Not Matched', category='errors')
        else:
            new_user =User(company_name = company_name, Full_Name = Full_Name, phone_number = phone_number, email = email, password = generate_password_hash(password, method='sha256'))
            try:
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                #flash('Account created successfully. Please log in.', category='success')
                return redirect(url_for('auth.login'))
            except IntegrityError as e:
                db.session.rollback()
                flash('Email already exists. Please choose a different email.', category='errors')
    return render_template("signup.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect (url_for('index.home'))
