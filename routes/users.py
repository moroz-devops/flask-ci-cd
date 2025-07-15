from flask import Blueprint, render_template
from models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def users_route():
    users = User.query.all()
    return render_template('users.html', users=users)

