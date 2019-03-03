from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from Jim import app, bcrypt, db
from Jim.forms import RegistrationForm, LoginForm
from Jim.models import User


@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# Route for registration
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # If user is authenticated redirect to home
    if current_user.is_authenticated:
        return redirect(url_for("home.html"))
    form = RegistrationForm
    # If the form validates then user's data is registered within database
    if form.validate_on_submit:
        # Hashing the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Setting data into model variables from registration form
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Committing data from form into database and redirecting to home
        db.session.add(user)
        db.commit()
        flash("Your account has been created!", 'success')
        return redirect(url_for("home.html"))
    # If user fails to register, redirect to signup template
    return render_template(url_for("signup.html"), title="Sign Up", form=form)


# Route for login
@app.route("/layout", methods=['GET', 'POST'])
def layout():
    # If user is authenticated redirect to home
    if current_user.is_authenticated:
        redirect(url_for("home.html"))
    form = LoginForm
    # If from validates, this function checks whether email and password match in database
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Remembers user's data, simplifies process of displaying user's data on template
            login_user(user, remember=form.remember.data)
            # Next page: the page user needs login to access
            next_page = request.args.get('next')
            # Leads user to page they couldn't access before login
            return redirect(next_page) if next_page else redirect(url_for("home.html"))
        # If form validation fails or email and password don't match, redirect to login
        else:
            flash("Login unsuccessful, please check email and password.", 'danger')
            return render_template(url_for("layout.html"), title='Login', form=form)


@app.route("/connect")
def connect():
    return render_template(url_for("connect.html"))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
