from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e23e8f9e119d62e3dc30b88fce520c54c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.database'
db = SQLAlchemy()
bcrypt = Bcrypt()

from Jim import routes
