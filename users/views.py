from flask import Blueprint, request, render_template, redirect

from .forms import UserCreateForm

user_pages = Blueprint('user_pages', __name__,
                        template_folder='templates')


@user_pages.route('/register', methods=['GET', 'POST'])
def register():
    '''
    View for register user
    '''
    register_form = UserCreateForm()

    if request.method == 'POST':
        register_form = UserCreateForm(request.form)

        if register_form.validate_on_submit():
            # todo: create user
            return redirect('/')

    return render_template('register.html', register_form=register_form)