import re
from flask import render_template, request, redirect, url_for, abort, flash, jsonify, Blueprint
from flask_login import current_user, login_required
from cafe_app.extensions import db
from cafe_app.contact.models import Contact
from cafe_app.menu.models import Category, Menu
from cafe_app.offer.models import Offer
from cafe_app.order.models import Cart, Order, Receipt
from cafe_app.table.models import Reserved, Table
from cafe_app.user.models import User
from cafe_app.core.utils import login_admin


core_blueprint = Blueprint('core', __name__)


@core_blueprint.route("/", methods=['POST', 'GET'])
def main():
    return render_template("home.html")


@core_blueprint.route('/our-story')
def our_story():
    return render_template('our-story.html')


@core_blueprint.route('/allmenu')
@login_admin
def all_menu():
    menu = Menu.query.all()
    return render_template('all-user.html', users=menu)


@core_blueprint.route('/all-message')
@login_admin
def all_message():
    contacts = Contact.query.all()
    return render_template('all-user.html', users=contacts)


@core_blueprint.route('/shop')
@login_required
def shop():
    cat = Category.query.all()
    return render_template('shop.html', cats=cat)


@core_blueprint.route('/purchase', methods=['POST'])
def purchase():
    purchase_data = request.get_json()
    if request.method == "POST":
        if purchase_data[0]["state"] == 'order_in_cafe':
            table_id = re.findall(r'\d+', purchase_data[0]["table"])[0]

            table_instance = Table.query.get(int(table_id))
            reserved_instance = Reserved(table_instance.id)
            db.session.add(reserved_instance)
            db.session.commit()

            reserved_instance_id = reserved_instance.id

        else:
            reserved_instance_id = None

        adderess = purchase_data[0]["address"]

        order_type = purchase_data[0]["state"]

        offer_instance = Offer.query.filter_by(offer_code=purchase_data[0]['offer_code']).first()
        offer_id = offer_instance.id if offer_instance else None

        receipt_instance = Receipt(float(purchase_data[0]['total-price'][:-2]), 0,
                                   float(purchase_data[0]['final-price'][:-2]))
        db.session.add(receipt_instance)
        db.session.commit()

        state = 'New orders'
        order_instance = Order(adderess, '', state, reserved_instance_id, receipt_instance.id, offer_id, order_type)

        db.session.add(order_instance)
        db.session.commit()
        cart_instance = Cart.query.filter_by(customer_id=current_user.id).filter_by(order_id=None).first()
        cart_instance.order_id = order_instance.id
        print(order_instance.id)
        db.session.commit()
        results = {'POST request': 'true'}
        return jsonify(results)
    else:
        return abort(400, 'Unsuccessful Transaction.')


@core_blueprint.route('/Terms-of-service')
def Terms_of_service():
    return render_template('Terms of service.html')


@core_blueprint.errorhandler(404)
def showError(error):
    return render_template("/errors/error_404.html"), 404


@core_blueprint.route('/add')
# @login_admin
def add_menu():
    c1 = Category('Category1', 'Description of Category1')
    c2 = Category('Category2', 'Description of Category2')
    c3 = Category('Category3', 'Description of Category3')
    c4 = Category('Category4', 'Description of Category4')
    c5 = Category('Category5', 'Description of Category5')

    m1 = Menu('Cake1', 120, 'Cake1 description', '1', 'static/shop/images/item01-768x768.png', True)
    m2 = Menu('Cake2', 135, 'Cake2 description', '1', 'static/shop/images/item02-768x768.jpg', True)
    m3 = Menu('Cake3', 140, 'Cake3 description', '1', 'static/shop/images/item03-768x768.jpg', True)
    m4 = Menu('Cake4', 85, 'Cake4 description', '1', 'static/shop/images/item04-768x768.png', True)
    m5 = Menu('Cake5', 105, 'Cake5 description', '2', 'static/shop/images/item02-768x768.jpg', True)
    m6 = Menu('Cake6', 92, 'Cake6 description', '2', 'static/shop/images/item03-768x768.jpg', True)
    m7 = Menu('Cake7', 98, 'Cake7 description', '2', 'static/shop/images/item01-768x768.png', True)

    off1 = Offer(50, 30, "off30")
    off2 = Offer(60, 40, "off40")

    m_list = [c1, c2, c3, c4, c5, m1, m2, m3, m4, m5, m6, m7, off1, off2]
    for m in m_list:
        db.session.add(m)
        db.session.commit()
    return 'added'


@core_blueprint.route('/addtable')
@login_admin
def add_table():
    table1 = Table(1, '1', 2)
    table2 = Table(2, '2', 2)
    table3 = Table(3, '3', 2)
    table4 = Table(4, '4', 4)
    table5 = Table(5, '5', 4)
    table6 = Table(6, '6', 4)
    table7 = Table(7, '7', 5)
    table8 = Table(8, '8', 6)

    m_list = [table1, table2, table3, table4, table5, table6, table7, table8]
    for m in m_list:
        db.session.add(m)
        db.session.commit()
    return 'added'


@core_blueprint.route('/add_admin')
def add_admin():
    admin = User('admin', 'adminian', 'admin@mail.ir', '1', character='admin')
    db.session.add(admin)
    db.session.commit()
    flash('add admin', 'info')
    return redirect(url_for('core.main'))
