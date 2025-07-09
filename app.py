from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return ''' 
    <h1>Hi! You are on a main page.</h1>
    <a href="/status">Status</a><br>
    <a href="/about">About</a><br>
    <a href="/hello">Hello</a><br>
    '''    

@app.route('/status')
def status():
    return jsonify({'status': 'ok'})
    
@app.route('/about')
def about():
    return '''
    <h1>About this site</h1>
    <p>This is my first Flask project with continious integration and deployment.<p>
    <a href="/">Back to main page</a>
    '''
@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'''
            <h1>Hello, {name}!</h1>
            <a href="/hello">Try again</a><br>
            <a href="/">Back to main page</a>
        '''
    return '''
        <h1>Enter your name:</h1>
        <form method="POST">
            <input type="text" name="name" required>
            <input type="submit" value="Submit">
            </form>
            <a href="/">Back to main page</a>
        '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
