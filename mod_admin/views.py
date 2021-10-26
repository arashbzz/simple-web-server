from flask import render_template, redirect, url_for, request, flash, session
from . import admin
from mod_users.forms import LoginForm
from mod_users.models import Users
from mod_admin.utils import admin_only_view
from main_page.models import SumDb


@admin.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate_on_submit:
            flash('error')
            return render_template('admin/login.html', form=form)

        user = Users.query.filter(
            Users.user_name == form.user_name.data).first()

        print(user)
        if user == None:
            flash('user name is incorrect ')
            return render_template('admin/login.html', form=form)

        if not user.check_password(user.password, form.password.data):
            flash('password is incorrect')
            return render_template('admin/login.html', form=form)
        if not user.is_admin():
            flash('you are not admin', 403)
            return render_template('admin/login.html', form=form)

        flash('you are login')
        session['user_id'] = user.id
        session['role'] = 1
        return redirect(url_for('admin.index'))

    if session.get('role') == 1:
        return redirect(url_for('admin.index'))

    return render_template('admin/login.html', form=form)


@admin.route('/')
@admin_only_view
def index():
    return render_template('admin/index.html')


@admin.route('/logout')
@admin_only_view
def logout():
    session.clear()
    return redirect(url_for('admin.login'))


@admin.route('/history', methods=['POST', 'GET'])
@admin_only_view
def history():
    history = SumDb.query.all()
    return render_template('admin/history.html', history=history)


@admin.route('/total', methods=['POST', 'GET'])
@admin_only_view
def total():
    history = SumDb.query.all()
    return render_template('admin/total.html', history=history)
