from flask import Blueprint, request, render_template
import sqlite3

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello', methods=['GET', 'POST'])

def hello_route():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        
        #check valid
        if not name:
            return render_template('hello.html', error="Name cannot be empty.")
        if len(name) < 3 or len(name) > 20:
            return render_template('hello.html', error="Name must be 3–20 characters long.")
        #repetition check
        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            conn.close()
            return render_template('hello.html', name_exists=name)
            
        #registration
        cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        
        return render_template('hello.html', name=name)

    return render_template('hello.html')
