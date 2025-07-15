from flask import Blueprint, request, render_template
from models import db, User

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
        existing_user = User.query.filter_by(name=name).first()
        
        if existing_user:
            return render_template('hello.html', name_exists=name)
            
        #registration
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        
        return render_template('hello.html', name=name)

    return render_template('hello.html')
