from flask import request, abort, jsonify, Blueprint
from cafe_app.offer.models import Offer
from cafe_app.static.shop.methods import get_all_offer_info

offer_blueprint = Blueprint('offer', __name__)


@offer_blueprint.route('/check-offer-code', methods=['GET', 'POST'])
def check_code():
    if request.method == "POST":
        cart_data = request.get_json()
        try:
            if offer_instance := Offer.query.filter_by(offer_code=cart_data['code']).first():
                results = get_all_offer_info(offer_instance)
                return jsonify(results)
        except Exception as ex:
            return str(ex)
        return abort(400, 'Offer Code not found!')



