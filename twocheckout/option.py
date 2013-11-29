from .api_request import Api
from .twocheckout import Twocheckout


class Option(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def create(cls, params={}):
        return cls(Api.call('products/create_option', params))

    @classmethod
    def find(cls, params={}):
        option = cls(Api.call('products/detail_option', params))
        return option.option[0]

    @classmethod
    def list(cls, params={}):
        list = cls(Api.call('products/list_options', params))
        return list.options

    def update(self, params={}):
        params['option_id'] = self.option_id
        Api.call('products/update_option', params)
        option = Option(Api.call('products/detail_option', params))
        return option.option[0]

    def delete(self, params={}):
        params['option_id'] = self.option_id
        return Option(Api.call('products/delete_option', params))
