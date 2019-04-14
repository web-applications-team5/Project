
from flask import jsonify

from app import app
from app.api.exception.Exceptions import NotFoundError
from app.entity.entities import Restaurant, Photo
from app.model.result_schemas import RestaurantSchema, PhotoSchema


@app.route("/api/v1/restaurants")
def retrieve_restaurents():
    restaurantSchema = RestaurantSchema(many=True)
    restaurants = Restaurant.query.all()
    restaurentsInfo = restaurantSchema.dump(restaurants)
    # restaurentsInfo = restaurantSchema.dump(Restaurant(id=12, name="test"))
    return jsonify(restaurants=restaurentsInfo.data)


@app.route("/api/v1/restaurants/<restaurantId>")
def retrieve_single_restaurent(restaurantId):  # noqa: E501

    restaurantSchema = RestaurantSchema()

    restaurant = Restaurant.query.get(restaurantId)
    if not restaurant:
        raise NotFoundError('Restaurant not found for provided restaurant-id.', status_code=404)

    return restaurantSchema.jsonify(restaurant)


@app.route("/api/v1/restaurants/<restaurantId>/photos")
def retrieve_restaurent_photos(restaurantId):  # noqa: E501

    restaurant = Restaurant.query.get(restaurantId)
    if not restaurant:
        raise NotFoundError('Restaurant not found for provided restaurant-id.', status_code=404)

    photoSchema = PhotoSchema(many=True)

    photos = Photo.query.filter_by(restaurant_id=restaurantId).all()
    photosInfo = photoSchema.dump(photos)

    return jsonify(photos=photosInfo.data)