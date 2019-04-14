import uuid

from flask import request

from app import app
from app.api.exception.Exceptions import NotFoundError
from app.model.result_schemas import OrderInfoSchema, Restaurant, OrderUser, Order, db, MenuItem, OrderItem
from app.model.response_models import OrderInfo
from datetime import datetime, timedelta

@app.route("/api/v1/restaurants/<restaurantId>/order", methods=["POST"])
def submit_order(restaurantId):  # noqa: E501

    order_schema = OrderInfoSchema()

    orderRequest = request.json

    restaurant = Restaurant.query.get(restaurantId)
    if not restaurant:
        raise NotFoundError('Restaurant not found for provided restaurant-id.', status_code=404)

    conf_number = uuid.uuid4().__str__()

    usr = OrderUser(name=orderRequest['name'], phone=orderRequest['phone'], email=orderRequest['email'])
    order = Order(user=usr, confirmationNumber=conf_number)

    db.session.add(usr)
    db.session.add(order)

    for item in orderRequest['menuItems']:
        menu_item = MenuItem.query.get(int(item['id']))
        db.session.add(OrderItem(order=order, menuItem=menu_item, quantity=item['quantity']))

    db.session.commit();

    order_info = OrderInfo(
        confirmation_number=conf_number,
        order_time='{:%Y-%m-%d T %H:%M:%S}'.format(datetime.now()),
        finish_time='{:%Y-%m-%d T %H:%M:%S}'.format(datetime.now() + timedelta(hours=1)),
        restaurant_info=restaurant
    )

    return order_schema.jsonify(order_info)