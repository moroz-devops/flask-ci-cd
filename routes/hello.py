import sqlite3
from flask import request

def hello_route():
    if request.method == 'POST':
        name = request.form.get('name').strip()

        if not name:
            return '''
                <h1>Name cannot be empty!</h1>
                <a href="/hello">Try again</a><br>
                <a href="/">Back to main page</a>
            '''

        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()

        # Перевірка наявності імені
        cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return f'''
                <h1>User "{name}" already exists!</h1>
                <a href="/hello">Try another name</a><br>
                <a href="/">Back to main page</a>
            '''

        # Якщо немає — додати
        cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

        return f'''
            <h1>Welcome, {name}! You are registered.</h1>
            <a href="/">Back to main page</a>
        '''

    # GET-запит — форма
    return '''
        <h1>Register</h1>
        <form method="POST">
            <input type="text" name="name" required>
            <input type="submit" value="Register">
        </form>
        <a href="/">Back to main page</a>
    '''
