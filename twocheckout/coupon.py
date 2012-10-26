from api_request import Api
from twocheckout import Twocheckout


class Coupon(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def create(cls, params=None):
        if params is None:
            params = dict()
        return cls(Api.call('products/create_coupon', params))

    @classmethod
    def find(cls, params=None):
        if params is None:
            params = dict()
        result = cls(Api.call('products/detail_coupon', params))
        return result.coupon

    @classmethod
    def list(cls, params=None):
        if params is None:
            params = dict()
        return cls(Api.call('products/list_coupons', params))

    def update(self, params=None):
        if params is None:
            params = dict()
        params['coupon_code'] = self.coupon_code
        Api.call('products/update_coupon', params)
        coupon = Coupon(Api.call('products/detail_coupon', params))
        return coupon.coupon

    def delete(self, params=None):
        if params is None:
            params = dict()
        params['coupon_code'] = self.coupon_code
        return Coupon(Api.call('products/delete_coupon', params))
