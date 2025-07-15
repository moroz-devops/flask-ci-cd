from flask import Flask, request, render_template
from database import init_db, db
from models import User

from routes.hello import hello_bp
from routes.status import status_bp
from routes.users import users_bp

app = Flask(__name__)
init_db(app) #initialize database
print("📡 DATABASE URI:", app.config['SQLALCHEMY_DATABASE_URI'])

#Blueprint register
app.register_blueprint(hello_bp)
app.register_blueprint(status_bp)
app.register_blueprint(users_bp)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

#Create new db tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
