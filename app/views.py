from . import app

from flask import Blueprint, render_template

core_pages = Blueprint('core_pages', __name__,
                        template_folder='templates')


@core_pages.route('/')
def index():
    return render_template('index.html')