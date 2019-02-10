from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html", title="Welcome")


@app.route("/detail")
def detail():
    return render_template("detail.html", title="Detail")


@app.route("/login")
def login():
    return render_template("login.html", title="Login")


@app.route("/SignUp")
def signup():
    return render_template("signup.html", title="Sign Up")


@app.route("/home")
def home():
    return render_template("home.html", title="Home")


if __name__ == '__main__':
    app.run(debug=True)

