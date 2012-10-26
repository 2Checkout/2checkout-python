from api_request import Api
from twocheckout import Twocheckout


class Contact(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def retrieve(cls, params=None):
        if params is None:
            params = dict()
        url = 'acct/detail_contact_info'
        response = cls(Api.call(url, params))
        return response.vendor_contact_info
