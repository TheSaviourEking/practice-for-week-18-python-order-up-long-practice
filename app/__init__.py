from flask import Flask
from .routes import orders, session
from .config import Configuration
from .models import db, Employee
from flask_login import LoginManager, login_user, current_user


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)
db.init_app(app)  # Configure the application with SQLAlchemy

login = LoginManager(app)
login.login_view = "session.login"  # login manager use the session.login bp function


# login manager uses load_user function to get employees for the db
@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
