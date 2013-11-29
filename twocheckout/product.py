from .api_request import Api
from .twocheckout import Twocheckout


class Product(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def create(cls, params={}):
        return cls(Api.call('products/create_product', params))

    @classmethod
    def find(cls, params={}):
        result = cls(Api.call('products/detail_product', params))
        return result.product

    @classmethod
    def list(cls, params={}):
        result = cls(Api.call('products/list_products', params))
        return result.products

    def update(self, params={}):
        params['product_id'] = self.product_id
        Api.call('products/update_product', params)
        product = Product(Api.call('products/detail_product', params))
        return product.product

    def delete(self, params={}):
        params['product_id'] = self.product_id
        return Product(Api.call('products/delete_product', params))
