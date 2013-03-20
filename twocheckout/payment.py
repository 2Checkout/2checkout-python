from .api_request import Api
from .twocheckout import Twocheckout


class Payment(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def pending(cls, params=None):
        if params is None:
            params = dict()
        url = 'acct/detail_pending_payment'
        response = cls(Api.call(url, params))
        return response.payment

    @classmethod
    def list(cls, params=None):
        if params is None:
            params = dict()
        url = 'acct/list_payments'
        response = cls(Api.call(url, params))
        return response.payments
