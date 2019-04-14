

class OrderInfo:

    def __init__(self, confirmation_number, order_time, restaurant_info, finish_time=None):
        self.confirmation_number = confirmation_number
        self.order_time = order_time
        self.restaurant_info = restaurant_info
        self.finish_time = finish_time