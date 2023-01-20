from cafe_app.menu.models import Menu
from cafe_app.offer.models import Offer
import json

def list2jsonstr(cart: str, data: list, flag: str) -> str:
    update_cart = False
    new_cart = []
    if cart: # if there is a cart
        old_cart = json.loads(cart)
        for dic in old_cart:
            # if (there was the item in old_cart) and (item_quantity != 0)
            if dic["id"] == str(data[0]["id"]):
                if flag == 'delete':
                    update_cart = True
                elif (flag == 'update') and (data[0]["quantity"] != 0):
                    new_cart.append(data[0])
                    update_cart = True
            else:
                new_cart.append(dic)
    # if (there isn't a cart) or (add new id of item) and (item_quantity != 0)
    if not update_cart and (data[0]["quantity"] != 0):
        new_cart.append(data[0])            
    result = json.dumps(new_cart)
    return result

def get_all_cart_info(cart: str):
    full_info = []
    json_cart = json.loads(cart)
    for item in json_cart:
        item_instance = Menu.query.get(int(item["id"]))
        item_info = {
            "id": item["id"],
            "name": item_instance.name,
            "quantity": item["quantity"],
            "price": item_instance.price,
            }
        full_info.append(item_info)
    result = json.dumps(full_info)
    return result

def get_all_offer_info(offer: Offer):
    full_info = {
        "percent": offer.percent,
        "min_price": offer.min_price,
        "max_price": offer.max_price,
        "expire_count": offer.expire_count,
        "expire_time": offer.expire_time.strftime("%d-%m-%Y"),
        }
    result = json.dumps(full_info)
    return result
        