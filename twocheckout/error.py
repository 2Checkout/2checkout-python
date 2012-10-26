class TwocheckoutError(Exception):
    def __init__(self, code=None, msg=None, product_id=None, option_id=None, coupon_code=None):
        super(TwocheckoutError, self).__init__(msg)
        self.code = code
        self.msg = msg
        self.product_id = product_id
        self.option_id = option_id
        self.coupon_code = coupon_code
