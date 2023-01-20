import json
from flask import request, jsonify, Blueprint
from cafe_app.extensions import db
from cafe_app.menu.models import Category, Menu
from cafe_app.core.utils import login_admin

menu_blueprint = Blueprint('menu', __name__)

############################ category #######################################
@menu_blueprint.route('/send-categories')
@login_admin
def send_categories():
    categories = Category.query.all()
    l = []
    for c in categories:
        c = vars(c)
        c.pop('_sa_instance_state')
        l.append(c)
    return jsonify(l)


@menu_blueprint.route('/new-category', methods=['POST', 'GET'])
@login_admin
def new_category():
    try:
        name = request.form['c-name']
        description = request.form['c-description']
        category = Category(name, description)
        db.session.add(category)
        db.session.commit()
        message = {'message': 'new category added'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@menu_blueprint.route('/del-category', methods=['POST'])
@login_admin
def del_category():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        category = Category.query.filter_by(id=id).first()
        db.session.delete(category)
        db.session.commit()
        message = {'message': f'category {id} deleted'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@menu_blueprint.route('/send-category', methods=['POST'])
@login_admin
def send_category():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        category = Category.query.filter_by(id=id).first()
        category = vars(category)
        category.pop('_sa_instance_state')
        return jsonify(category)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@menu_blueprint.route('/update-category', methods=['POST'])
@login_admin
def update_category():
    try:
        id = request.form['c-id']
        category = Category.query.filter_by(id=id).first()
        category.name = request.form['c-e-name']
        category.description = request.form['c-e-description']
        db.session.commit()
        message = {'message': 'Update done'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


###########################################################################################
##################################### Menu Items #########################################
@menu_blueprint.route('/send-menus')
@login_admin
def send_menus():
    menus = Menu.query.all()
    l = []
    for m in menus:
        m = vars(m)
        m.pop('_sa_instance_state')
        l.append(m)
    return jsonify(l)


@menu_blueprint.route('/new-menu', methods=['POST', 'GET'])
@login_admin
def new_menu():
    try:
        name = request.form['m-name']
        price = int(request.form['m-price'])
        picture_path = request.form['m-picture_path']
        category_id = request.form['m-category_id']
        description = request.form['m-description']
        menu = Menu(name, price, description, category_id, picture_path)
        db.session.add(menu)
        db.session.commit()
        message = {'message': 'new menu added'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@menu_blueprint.route('/del-menu', methods=['POST'])
@login_admin
def del_menu():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        menu = Menu.query.filter_by(id=id).first()
        db.session.delete(menu)
        db.session.commit()
        message = {'message': f'menu {id} deleted'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@menu_blueprint.route('/send-menu', methods=['POST'])
@login_admin
def send_menu():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        menu = Menu.query.filter_by(id=id).first()
        menu = vars(menu)
        menu.pop('_sa_instance_state')
        return jsonify(menu)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@menu_blueprint.route('/update-menu', methods=['POST'])
@login_admin
def update_menu():
    try:
        id = request.form['m-id']
        menu = Menu.query.filter_by(id=id).first()
        menu.name = request.form['m-e-name']
        menu.price = int(request.form['m-e-price'])
        menu.category_id = request.form['m-e-category_id']
        menu.picture_path = request.form['m-e-picture_path']
        menu.status = True if request.form['m-e-status'] == 'true' else False
        menu.description = request.form['m-e-description']
        db.session.commit()
        message = {'message': 'Update done'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)

