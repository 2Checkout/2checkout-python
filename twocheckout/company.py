from twocheckout import Twocheckout


class Company(Twocheckout):
    @classmethod
    def retrieve(cls, api, params=None):
        if params is None:
            params = dict()
        url = 'acct/detail_company_info'
        response = cls(api.call(url, params), api=api)
        return response.vendor_company_info
