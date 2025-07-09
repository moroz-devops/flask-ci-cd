import sqlite3

def users_route():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users')
    users = cursor.fetchall()
    conn.close()

    users_html = "<ul>"
    for user in users:
        users_html += f"<li>{user[0]}</li>"
    users_html += "</ul>"

    return f'''
        <h1>Registered Users</h1>
        {users_html}
        <a href="/">Back to main page</a>
    '''

