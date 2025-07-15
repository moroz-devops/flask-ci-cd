from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Завантажує .env файл

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

