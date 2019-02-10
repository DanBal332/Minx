import dt


class User(dt.Model):
    username = dt.Column(dt.String(15), unique=True, nullable=False)
    email = dt.Column(dt.String(100), unique=True, nullable=False)
    password = dt.Column(dt.String(60), nullable=False)
    confirm_password = dt.Column(dt.String(60), nullable=False)
