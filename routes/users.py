from flask import Blueprint, render_template
import sqlite3

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')

def users_route():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users')
    users_list = cursor.fetchall()
    conn.close()
    
    return render_template('users.html', users=users_list)

