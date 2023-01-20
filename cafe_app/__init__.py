from flask import Flask
from cafe_app.order.routes import order_blueprint
from cafe_app.user.routes import user_blueprint
from cafe_app.table.routes import table_blueprint
from cafe_app.menu.routes import menu_blueprint
from cafe_app.offer.routes import offer_blueprint
from cafe_app.core.routes import core_blueprint
from cafe_app.contact.routes import contact_blueprint
from cafe_app.extensions import db, login_manager


def register_blueprint(app: Flask):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(offer_blueprint)
    app.register_blueprint(order_blueprint)
    app.register_blueprint(core_blueprint)
    app.register_blueprint(contact_blueprint)
    app.register_blueprint(table_blueprint)
    app.register_blueprint(menu_blueprint)


app = Flask(__name__)
app.config.from_object('config.DevConfig')
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'users.sign_in'
login_manager.login_message_category = 'info'


register_blueprint(app)


import cafe_app.user.models
import cafe_app.order.models
import cafe_app.menu.models
import cafe_app.offer.models
import cafe_app.contact.models
import cafe_app.table.models

with app.app_context():
    db.create_all()

# migrate.init_app(app, db)
