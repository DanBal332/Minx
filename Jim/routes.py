from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required
from Jim import app
from Jim.models import User
from Jim.forms import RegistrationForm, LoginForm
from Jim import db, bcrypt


@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html", title="Welcome")


@app.route("/detail")
def detail():
    return render_template("detail.html", title="Detail")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_required(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
            return render_template('login.html', title='Login', form=form)


@app.route("/home")
def home():
    return render_template("home.html", title="Home")


if __name__ == '__main__':
    app.run(debug=True)
