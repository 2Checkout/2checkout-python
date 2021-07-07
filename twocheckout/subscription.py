from twocheckout import Api
from twocheckout import response


# full docs about order here: https://app.swaggerhub.com/apis-docs/2Checkout-API/api-rest_documentation/6.0#/Order
class Subscription(Api):

    def __init__(self, params):
        Api.__init__(self, params)
        self.set_resource('subscriptions')

    # get an order full info bu 2Checkout transaction ID (RefNo)
    # more info here: https://app.swaggerhub.com/apis-docs/2Checkout-API/api-rest_documentation/6.0#/Subscription/get_subscriptions__SubscriptionReference__
    def get(self, subscription_reference):
        result = self.call(self.get_resource() + subscription_reference + '/', None, 'get')

        return response.parse(result)

    # place a new order using the params provided
    # for more information about the params you can visit our docs
    # https://app.swaggerhub.com/apis-docs/2Checkout-API/api-rest_documentation/6.0#/Subscription/post_subscriptions_
    def create(self, data):
        result = self.call(self.get_resource(), data)

        return response.parse(result)
