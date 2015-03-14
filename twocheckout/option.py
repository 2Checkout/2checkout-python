from twocheckout import Twocheckout


class Option(Twocheckout):
    @classmethod
    def create(cls, api, params=None):
        if params is None:
            params = dict()
        return cls(api.call('products/create_option', params), api=api)

    @classmethod
    def find(cls, api, params=None):
        if params is None:
            params = dict()
        option = cls(api.call('products/detail_option', params), api=api)
        return option.option[0]

    @classmethod
    def list(cls, api, params=None):
        if params is None:
            params = dict()
        list = cls(api.call('products/list_options', params), api=api)
        return list.options

    def update(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['option_id'] = self.option_id
        api.call('products/update_option', params)
        option = Option(api.call('products/detail_option', params), api=api)
        return option.option[0]

    def delete(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['option_id'] = self.option_id
        return Option(api.call('products/delete_option', params), api=api)
