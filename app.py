from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi! You are on a main page'

@app.route('/status')
def status():
    return jsonify({'status': 'ok'})

@app.route('/hello/<name>')
def hello(name):
    return f'Привіт, {name}!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
