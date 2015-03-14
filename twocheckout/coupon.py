from twocheckout import Twocheckout


class Coupon(Twocheckout):
    @classmethod
    def create(cls, api, params=None):
        if params is None:
            params = dict()
        return cls(api.call('products/create_coupon', params), api=api)

    @classmethod
    def find(cls, api, params=None):
        if params is None:
            params = dict()
        result = cls(api.call('products/detail_coupon', params), api=api)
        return result.coupon

    @classmethod
    def list(cls, api, params=None):
        if params is None:
            params = dict()
        return cls(api.call('products/list_coupons', params), api=api)

    def update(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['coupon_code'] = self.coupon_code
        api.call('products/update_coupon', params)
        coupon = Coupon(api.call('products/detail_coupon', params), api=api)
        return coupon.coupon

    def delete(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['coupon_code'] = self.coupon_code
        return Coupon(api.call('products/delete_coupon', params), api=api)
