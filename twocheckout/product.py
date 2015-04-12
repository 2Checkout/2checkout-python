from twocheckout import Twocheckout


class Product(Twocheckout):
    @classmethod
    def create(cls, api, params=None):
        if params is None:
            params = dict()
        return cls(api.call('products/create_product', params), api=api)

    @classmethod
    def find(cls, api, params=None):
        if params is None:
            params = dict()
        result = cls(api.call('products/detail_product', params), api=api)
        return result.product

    @classmethod
    def list(cls, api, params=None):
        if params is None:
            params = dict()
        result = cls(api.call('products/list_products', params), api=api)
        return result.products

    def update(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['product_id'] = self.product_id
        api.call('products/update_product', params)
        product = Product(api.call('products/detail_product', params), api=api)
        return product.product

    def delete(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['product_id'] = self.product_id
        return Product(api.call('products/delete_product', params), api=api)
