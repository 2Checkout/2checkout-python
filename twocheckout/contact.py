from twocheckout import Twocheckout


class Contact(Twocheckout):
    @classmethod
    def retrieve(cls, api, params=None):
        if params is None:
            params = dict()
        url = 'acct/detail_contact_info'
        response = cls(api.call(url, params), api=api)
        return response.vendor_contact_info
