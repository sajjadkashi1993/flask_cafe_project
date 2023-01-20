import functools
from flask_login import current_user, login_required
from flask import abort

def login_admin(func):
    @functools.wraps(func)
    @login_required
    def wrapper_dec(*args, **kwargs):
        if current_user.character == 'admin':
            return func(*args, **kwargs)
        else:
            return abort(404, 'not find')
    return wrapper_dec