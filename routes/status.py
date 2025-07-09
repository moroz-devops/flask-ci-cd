from flask import jsonify

def status_route():
    return jsonify({'status': 'ok'})
