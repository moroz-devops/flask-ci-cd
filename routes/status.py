from flask import Blueprint, render_template

status_bp = Blueprint('status', __name__)

@status_bp.route('/status')

def status_route():
    return render_template("status.html")
