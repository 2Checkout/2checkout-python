from api_request import Api
from twocheckout import Twocheckout


class Option(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def create(cls, params=None):
        if params is None:
            params = dict()
        return cls(Api.call('products/create_option', params))

    @classmethod
    def find(cls, params=None):
        if params is None:
            params = dict()
        option = cls(Api.call('products/detail_option', params))
        return option.option[0]

    @classmethod
    def list(cls, params=None):
        if params is None:
            params = dict()
        list = cls(Api.call('products/list_options', params))
        return list.options

    def update(self, params=None):
        if params is None:
            params = dict()
        params['option_id'] = self.option_id
        Api.call('products/update_option', params)
        option = Option(Api.call('products/detail_option', params))
        return option.option[0]

    def delete(self, params=None):
        if params is None:
            params = dict()
        params['option_id'] = self.option_id
        return Option(Api.call('products/delete_option', params))
