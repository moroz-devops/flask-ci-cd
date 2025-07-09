from flask import Flask, jsonify, request
from database import init_db
import sqlite3

from routes.home import home_route
from routes.status import status_route
from routes.about import about_route
from routes.hello import hello_route
from routes.users import users_route

app = Flask(__name__)
init_db() #initialize database

@app.route('/')
def home():
    return home_route()

@app.route('/status')
def status():
    return status_route()
    
@app.route('/about')
def about():
    return about_route()

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return hello_route()

@app.route('/users')
def users():
    return users_route()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
