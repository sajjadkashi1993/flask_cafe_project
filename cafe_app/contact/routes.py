import json
from flask import render_template, request, jsonify, Blueprint
from cafe_app.extensions import db
from cafe_app.contact.forms import ContactForm
from cafe_app.contact.models import Contact

contact_blueprint = Blueprint('contact', __name__)


@contact_blueprint.route("/contact", methods=['POST', 'GET'])
def contact():
    contact_form = ContactForm()
    if request.method == "POST":
        if contact_form.validate_on_submit():
            try:
                contact_first_name = contact_form.first_name.data
                contact_last_name = contact_form.last_name.data
                contact_email = contact_form.email.data
                contact_phone = contact_form.phone.data
                contact_message = contact_form.message.data
                # contact_captcha = contact_form.agree_chaptcha.data
                contact = Contact(contact_first_name, contact_last_name, contact_email, contact_phone, contact_message)
                db.session.add(contact)
                db.session.commit()
                message = {'message': 'Send it your masseg'}
                return jsonify(message)
            except Exception as ex:
                message = {'message': "Sorry that's message did'nt send :" + str(ex)}
                return jsonify(message)
        else:
            return jsonify(contact_form.errors)
    return render_template('Contact.html', contact_form=contact_form)


########################################################################################
##################################### contact #########################################
@contact_blueprint.route('/send-contact')
def send_contact():
    contacts = Contact.query.all()
    l = []
    for c in contacts:
        c = vars(c)
        c.pop('_sa_instance_state')
        l.append(c)
    return jsonify(l)


@contact_blueprint.route('/del-contact', methods=['POST'])
def del_contact():
    try:
        d = json.loads(request.data)
        id = int(d['id'])
        c = Contact.query.filter_by(id=id).first()
        db.session.delete(c)
        db.session.commit()
        message = {'message': f'contact us {id} deleted'}
        return jsonify(message)
    except Exception as ex:
        message = {'message': "متاسفانه تغییرات انجام نشد" + "\n" + str(ex)}
        return jsonify(message)
