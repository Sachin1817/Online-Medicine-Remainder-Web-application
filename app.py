from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config
from scheduler import start_scheduler
from models import db
import os

login_manager = LoginManager()
mail = Mail()
scheduler = BackgroundScheduler()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    with app.app_context():
        db.create_all()

    # Import and register blueprints
    from routes.auth import auth_bp
    from routes.medicines import medicines_bp
    from routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(medicines_bp)
    app.register_blueprint(admin_bp)

    # Start scheduler
    start_scheduler(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
