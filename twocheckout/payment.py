from .twocheckout import Twocheckout


class Payment(Twocheckout):
    @classmethod
    def pending(cls, api, params=None):
        if params is None:
            params = dict()
        url = 'acct/detail_pending_payment'
        response = cls(api.call(url, params), api=api)
        return response.payment

    @classmethod
    def list(cls, api, params=None):
        if params is None:
            params = dict()
        url = 'acct/list_payments'
        response = cls(api.call(url, params), api=api)
        return response.payments
