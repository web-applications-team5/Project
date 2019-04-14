import datetime
import uuid

from faker import Factory

import random
from datetime import datetime, timedelta

from app.entity import db
from app.entity.entities import Address, Menu, MenuItem, OrderItem, Order, Photo, Restaurant, OrderUser


def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

def addEntityAndCommit(fentity, *entityArgs):
    db.session.add(fentity);
    for entity in entityArgs:
        db.session.add(entity);

# Food item urls

fake = Factory.create()

db.drop_all();
db.create_all();

address = Address(id=1, addressLine="123s test street", city="dummy city", state='WA', zipcode="12345");
restaurant = Restaurant(id=1, name="test restaurant", openTime=datetime(2019, 1, 1, 8, 0, 0).time(),
                        closeTime=datetime(2019, 1, 1, 20, 0, 0).time(), logo=None, description=None,
                        rating=None, address_id=1, address=address);
menu = Menu(id=1, restaurant_id=1, restaurant=restaurant)
photo = Photo(id=1, url='test', restaurant_id=1, restaurant=restaurant)

menuItem1 = MenuItem(id=1, name='VED MOMOS', price=7.75, description=None,
                    photo='snacks_vegmomo.jpg', status='ACTIVE', menu_id=1, menu=menu)
menuItem2 = MenuItem(id=2, name='Chicken Momos', price=10.5, description=None,
                    photo='snacks_nonvegmomo.jpg', status='ACTIVE', menu_id=1, menu=menu)
menuItem3 = MenuItem(id=3, name='Fried Veg Momos', price=8.5, description=None,
                    photo='snacks_fryvegmomo.jpg', status='ACTIVE', menu_id=1, menu=menu)
menuItem4 = MenuItem(id=4, name='Fried Chicken Momos', price=7.75, description=None,
                    photo='snacks_frynonvegmomo.jpg', status='ACTIVE', menu_id=1, menu=menu)
menuItem5 = MenuItem(id=5, name='Veg Chowmin', price=6.25, description=None,
                    photo='snacks_chommeen.jpg', status='ACTIVE', menu_id=1, menu=menu)
menuItem6 = MenuItem(id=6, name='Veg Spring Roll', price=4.5, description=None,
                    photo='snacks_vegroll.jpg', status='ACTIVE', menu_id=1, menu=menu)

addEntityAndCommit(address, menu, restaurant, photo, menuItem1, menuItem2, menuItem3, menuItem4, menuItem5, menuItem6);

# orderCounter = 1
# itemCounter = 1
# for num in range(100):
#
#     user = OrderUser(id=num, name=fake.name(), phone='242-555-0101', email='test@email.com');
#     addEntityAndCommit(user);
#
#     for num2 in range(10):
#
#         order = Order(id=orderCounter, status='ACTIVE', createdDate=gen_datetime(2019, 2019),
#                       user_id=num2, user=user, confirmationNumber=uuid.uuid4().__str__());
#         addEntityAndCommit(order);
#
#         for num3 in range(5):
#             menuItem = MenuItem(id=itemCounter, name=fake.name(), price=random.randint(5, 25), description=None,
#                                 photo='test', status='ACTIVE', menu_id=1, menu=menu)
#             orderItem = OrderItem(id=itemCounter, order_id=orderCounter, menuItem_id=itemCounter, menuItem=menuItem,
#                                   order=order)
#             itemCounter = itemCounter + 1;
#             addEntityAndCommit(menuItem, orderItem);
#
#         orderCounter = orderCounter + 1
#
#     for num4 in range(10):
#
#         order = Order(id=orderCounter, status='ACTIVE', createdDate=gen_datetime(2019, 2019),
#                       user_id=num2, user=user);
#
#         for num5 in range(5):
#             menuItem = MenuItem(id=itemCounter, name=fake.name(), price=random.randint(5, 25), description=None,
#                                 photo='test', status='ACTIVE', menu_id=1, menu=menu)
#             orderItem = OrderItem(id=itemCounter, order_id=orderCounter, menuItem_id=itemCounter, menuItem=menuItem,
#                                   order=order)
#             itemCounter = itemCounter + 1;
#             addEntityAndCommit(menuItem, orderItem);
#
#         orderCounter = orderCounter + 1

db.session.commit();