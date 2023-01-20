import json
from flask import request, jsonify, Blueprint
from flask_login import current_user
from cafe_app.extensions import db
from cafe_app.order.models import Cart, Order, Receipt
from cafe_app.static.shop.methods import list2jsonstr, get_all_cart_info
from cafe_app.core.utils import login_admin

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/send-orders')
@login_admin
def send_orders():
    orders = Order.query.all()
    l = []
    for o in orders:
        o = vars(o)
        o.pop('_sa_instance_state')
        l.append(o)
    return jsonify(l)


@order_blueprint.route('/send-order', methods=['POST'])
@login_admin
def send_order():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        order = Order.query.filter_by(id=id).first()
        order = vars(order)
        order.pop('_sa_instance_state')
        return jsonify(order)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@order_blueprint.route('/update-order', methods=['POST'])
@login_admin
def update_order():
    try:
        id = request.form['o-id']
        order = Order.query.filter_by(id=id).first()
        order.state = request.form['o-e-state']
        db.session.commit()
        message = {'message': 'Update done'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


########################################################################################
###################################### receipts ###########################################
@order_blueprint.route('/send-receipts')
@login_admin
def send_receipts():
    receipts = Receipt.query.all()
    print(receipts)
    l = []
    for r in receipts:
        r = vars(r)
        r.pop('_sa_instance_state')
        l.append(r)
        print(l)
    return jsonify(l)


#####################################################################################
################################ user order ########################################
@order_blueprint.route('/send-user-orders')
def send_user_orders():
    carts = current_user.carts
    orders = []
    for cart in carts:
        orders.append(cart.order)
    l = []
    for o in orders:
        o = vars(o)
        o.pop('_sa_instance_state')
        l.append(o)
    return jsonify(l)
#####################################################################################

@order_blueprint.route('/update-cart-data', methods=['GET', 'POST'])
def process_cart():
    if request.method == "POST":
        cart_data = request.get_json()
        try:
            if cart_instance := Cart.query.filter_by(customer_id=current_user.id).filter_by(order_id=None).first():
                new_items = list2jsonstr(cart_instance.item_quantity, cart_data, 'update')
                cart_instance.item_quantity = new_items
                db.session.commit()
            else:
                new_items = list2jsonstr("", cart_data, 'update')
                cart_instance = Cart(new_items, current_user.id)
                db.session.add(cart_instance)
                db.session.commit()
        except Exception as ex:
            return "Cart can not change due to" + "<br>" + str(ex)
        results = {'POST request': 'true'}
        return jsonify(results)
    if request.method == "GET":
        try:
            if cart_instance := Cart.query.filter_by(customer_id=current_user.id).filter_by(order_id=None).first():
                results = get_all_cart_info(cart_instance.item_quantity)
                print(results)
                return jsonify(results)
        except Exception as ex:
            return "UserCart can not update by DB due to" + "<br>" + str(ex)


@order_blueprint.route('/delete-cart-data', methods=['DELETE'])
def delete_item():
    if request.method == "DELETE":
        item_data = request.get_json()
        try:
            if cart_instance := Cart.query.filter_by(customer_id=current_user.id).filter_by(order_id=None).first():
                new_items = list2jsonstr(cart_instance.item_quantity, item_data, 'delete')
                cart_instance.item_quantity = new_items
                db.session.commit()
        except Exception as ex:
            return "Cart can not change due to" + "<br>" + str(ex)
        results = {'POST request': 'true'}
        return jsonify(results)
