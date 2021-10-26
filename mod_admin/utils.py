from flask import session, redirect, flash, url_for
from functools import wraps


def admin_only_view(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if session.get('user_id') is None:
            flash('abort', 401)
            return redirect(url_for('admin.login'))
        if session.get('role') != 1:
            flash('abort', 403)
            return redirect(url_for('admin.login'))
        return func(*args, **kwargs)

    return decorator
