from marshmallow import fields

from app.entity import ma
from app.entity.entities import *
from app.model.request_models import OrderRequest
from app.model.service_excpetions import ServiceException


class AddressSchema(ma.Schema):
    class Meta:
        # model = Address
        fields = ("addressLine", "city", "state", "zipcode")


class PhotoSchema(ma.Schema):
    class Meta:
        # model = Photo
        fields = ("url",)


class RestaurantSchema(ma.Schema):
    class Meta:
        # model = Restaurant
        # Fields to expose
        fields = ("id", "name", "openTime", "closeTime", "logo", "description", "rating", "address")

    address = ma.Nested(AddressSchema)


class MenuItemSchema(ma.ModelSchema):
    class Meta:
        model = MenuItem


class RestaurantMenuSchema(ma.Schema):
    class Meta:
        # model = Restaurant
        # Fields to expose
        fields = ("id", "menu")

    address = ma.Nested(AddressSchema)


class ServiceExceptionSchema(ma.Schema):
    class Meta:
        fields = ("code", "message", "details")


class OrderInfoSchema(ma.Schema):
    class Meta:
        fields = ("restaurant_info", "order_time", "finish_time", "confirmation_number")

    restaurant_info = ma.Nested(RestaurantSchema)

class OrderRequestSchema(ma.Schema):
    name = fields.Str(required=True)
    phone = fields.Str(required=True)
    email = fields.Email()
    menuItems = fields.List(fields.Int())