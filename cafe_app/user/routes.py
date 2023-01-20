from hashlib import sha256
from flask import render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from cafe_app.extensions import db
from cafe_app.user.forms import RegistrationForm, LogInForm, UpDate
from cafe_app.user.models import User
from cafe_app.core.utils import login_admin

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/signin', methods=['POST', 'GET'])
def sign_in():
    if current_user.is_authenticated:
        flash('you logged in before', 'warning')
        return redirect(url_for('core.main'))
    login_form = LogInForm()
    if request.method == "POST":
        user = User.query.filter_by(email=login_form.email.data).first()
        user_pass = login_form.password.data
        if user and user.password == sha256(user_pass.encode()).hexdigest():
            login_user(user, remember=login_form.remember.data)
            flash('you logged in successfully', 'success')
            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('core.main'))
        else:
            flash('Email or Password is wronged', 'danger')
    return render_template('login.html', login_form=login_form)


@user_blueprint.route('/signout')
@login_required
def signout():
    logout_user()
    flash('you logged out successfully', 'warning')
    return redirect(url_for('core.main'))


@user_blueprint.route('/signup', methods=['POST', 'GET'])
def sign_up():
    register_form = RegistrationForm()
    if request.method == "POST":
        if register_form.validate_on_submit():
            user_f_name = register_form.fname.data
            user_l_name = register_form.lname.data
            user_email = register_form.email.data
            user_pass = register_form.password.data
            try:
                user = User(user_f_name, user_l_name, user_email, user_pass)
                db.session.add(user)
                db.session.commit()
                flash('successful', 'success')
                return redirect(url_for('core.main'))
            except Exception as ex:
                return "متاسفانه ثبت نام شما انجام نشد" + "<br>" + str(ex)
    return render_template('signup.html', register_form=register_form)


@user_blueprint.route('/user-dashboard', methods=['POST', 'GET'])
@login_required
def user_dashboard():
    update_form = UpDate()
    if request.method == 'POST':
        if update_form.validate_on_submit():
            try:
                current_user.f_name = update_form.fname.data
                current_user.l_name = update_form.lname.data
                current_user.email = update_form.email.data
                current_user.address = update_form.address.data
                current_user.phone_number = update_form.phone_number.data
                db.session.commit()
                message = {'message': 'Update done'}
                return jsonify(message)
            except Exception as ex:
                message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
                return jsonify(message)
        else:
            return jsonify(update_form.errors)

    elif request.method == 'GET':
        update_form.fname.data = current_user.f_name
        update_form.lname.data = current_user.l_name
        update_form.email.data = current_user.email
        update_form.address.d = current_user.address
        update_form.phone_number.data = current_user.phone_number
        return render_template('user-dashboard.html', form=update_form)


@user_blueprint.route('/admin-dashboard')
@login_admin
def admin_dashboard():
    return render_template('admin-dashboard.html')


@user_blueprint.route('/all-user')
@login_admin
def all_user():
    users = User.query.all()
    return render_template('all-user.html', users=users)
