import json
from flask import request, jsonify, Blueprint
from cafe_app.extensions import db
from cafe_app.table.models import Table
from cafe_app.static.table.methods import get_all_table_info
from cafe_app.core.utils import login_admin

table_blueprint = Blueprint('table', __name__)


@table_blueprint.route('/new-table', methods=['POST', 'GET'])
@login_admin
def new_table():
    try:
        t_num = int(request.form['t-num'])
        position = request.form['position']
        t_spacing = int(request.form['t-spacing'])
        table = Table(t_num, position, t_spacing)
        db.session.add(table)
        db.session.commit()
        message = {'message': 'new table added'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@table_blueprint.route('/del-table', methods=['POST'])
@login_admin
def del_table():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        print(id, type(id))
        table = Table.query.filter_by(id=id).first()
        db.session.delete(table)
        db.session.commit()
        message = {'message': f'table {id} deleted'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@table_blueprint.route('/send-tables')
@login_admin
def send_tables():
    tables = Table.query.all()
    l = []
    for t in tables:
        t = vars(t)
        t.pop('_sa_instance_state')
        l.append(t)
    return jsonify(l)


@table_blueprint.route('/send-table', methods=['POST'])
@login_admin
def send_table():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        table = Table.query.filter_by(id=id).first()
        table = vars(table)
        table.pop('_sa_instance_state')
        return jsonify(table)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@table_blueprint.route('/update-table', methods=['POST'])
@login_admin
def update_table():
    try:
        id = request.form['t-id']
        table = Table.query.filter_by(id=id).first()
        table.table_number = request.form['t-num']
        table.position = request.form['position']
        table.table_spacing = request.form['t-spacing']
        db.session.commit()
        message = {'message': 'Update done'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)


@table_blueprint.route('/update-table-data', methods=['GET'])
def process_table():
    if request.method == "GET":
        try:
            if table_instances := Table.query.all():
                results = get_all_table_info(table_instances)
                return jsonify(results)
        except Exception as ex:
            return "UserCart can not update by DB due to" + "<br>" + str(ex)


