from flask import Flask, request, render_template
from database import init_db, db
from models import User

from routes.hello import hello_bp
from routes.status import status_bp
from routes.users import users_bp

from config import DevelopmentConfig, ProductionConfig
import os

def create_app():
    app = Flask(__name__)
    #Select environment
    env = os.getenv('FLASK_ENV', 'development')
    
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object(DevelopmentConfig)
    
    #initialize database
    init_db(app)

    #Blueprint routes register
    app.register_blueprint(hello_bp)
    app.register_blueprint(status_bp)
    app.register_blueprint(users_bp)

    #html pages
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    #Create new db tables
    with app.app_context():
        db.create_all()
        
    return app

#Start app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
