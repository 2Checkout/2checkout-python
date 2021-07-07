from twocheckout import Api
from twocheckout import response


# full docs about order here: https://app.swaggerhub.com/apis-docs/2Checkout-API/api-rest_documentation/6.0#/Order
class Order(Api):

    def __init__(self, params):
        Api.__init__(self, params)
        self.set_resource('orders')

    # get an order full info bu 2Checkout transaction ID (RefNo)
    # more info here: https://app.swaggerhub.com/apis-docs/2Checkout-API/api-rest_documentation/6.0#/Order/get_orders__OrderReference__
    def get(self, ref_no):
        result = self.call(self.get_resource() + ref_no + '/', None, 'get')

        return response.parse(result)

    # place a new order using the params provided
    # for more information about the params you can visit our docs
    # https://app.swaggerhub.com/apis-docs/2Checkout-API/api-rest_documentation/6.0#/Order/post_orders_
    def create(self, data):
        result = self.call(self.get_resource(), data)

        return response.parse(result)
