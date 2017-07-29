from flask import Blueprint, request, render_template, redirect

from .forms import UserCreateForm

from .models import User

from app import db

user_pages = Blueprint('user_pages', __name__,
                        template_folder='templates')


@user_pages.route('/register', methods=['GET', 'POST'])
def register():
    """
    View for register user
    :return:
    """

    register_form = UserCreateForm(request.form)

    if request.method == 'POST':
        if register_form.validate():
            user = User(request.form['username'],request.form['email'], \
                        request.form['password'])
            db.session.add(user)
            db.session.commit()
            return redirect('/')

    return render_template('register.html', register_form=register_form)