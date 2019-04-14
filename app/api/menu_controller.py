from flask import request, jsonify

from app import app
from app.api.exception.Exceptions import NotFoundError
from app.model.result_schemas import MenuItemSchema, Restaurant, MenuItem, Menu


@app.route("/api/v1/restaurants/<restaurantId>/menu")
def retrieve_restaurent_menu(restaurantId):

    menuItemSchema = MenuItemSchema(many=True)

    _page = 1 if not request.args.get('page') else int(request.args.get('page'));

    restaurant = Restaurant.query.get(restaurantId)
    if(not restaurant):
        raise NotFoundError('Restaurant not found for provided restaurant-id.', status_code=404)

    menus = Menu.query.filter(Menu.restaurant_id == restaurantId)
    if(not menus):
        raise NotFoundError('No menu found for the restaurant.', status_code=404)

    total_menuItems = MenuItem.query.filter(MenuItem.menu_id == menus[0].id).count()
    if(total_menuItems==0):
        return jsonify(restaurantId=restaurantId, menu={}, count=total_menuItems);

    menuItems = MenuItem.query.filter(MenuItem.menu_id == menus[0].id).paginate(page=_page, per_page=25).items
    menuItemsSerialized = menuItemSchema.dump(menuItems)
    return jsonify(restaurantId=restaurantId, menu=menuItemsSerialized.data, count=total_menuItems);

@app.route("/api/v1/item/<itemId>")
def retrieve_restaurent_menu_item(itemId):

    menuItemSchema = MenuItemSchema()

    item = MenuItem.query.get(itemId)
    if not item:
        raise NotFoundError('MenuItem not found for provided item-id.', status_code=404)

    return menuItemSchema.jsonify(item)

