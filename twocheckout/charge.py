import urllib

from twocheckout import Twocheckout


class Charge(Twocheckout):
    checkout_url = "https://www.2checkout.com/checkout/purchase"

    def __init__(self, dict_, api=None):
        super(Charge, self).__init__(dict_, api=api)
        if api.mode == 'sandbox':
            self.checkout_url = 'https://sandbox.2checkout.com/checkout/purchase'
        else:
            self.checkout_url = 'https://www.2checkout.com/checkout/purchase'

    def form(self, params=None, text='Proceed to Checkout'):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"" + self.checkout_url + "\" method=\"post\">"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />"
        return form + "<input type=\"submit\" value=\"" + text + "\" /></form>"

    def submit(self, params=None, text='Proceed to Checkout'):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"" + self.checkout_url + "\" method=\"post\">"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />"
        return form + "<input type=\"submit\" value=\"" + text + "\" /></form>" + \
            "<script type=\"text/javascript\">document.getElementById(\"2checkout\").submit();</script>"

    def direct(self, params=None, text='Proceed to Checkout'):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"" + self.checkout_url + "\" method=\"post\">"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />"
        return form + "<input type=\"submit\" value=\"" + text + "\" /></form>" + \
            "<script src=\"https://www.2checkout.com/static/checkout/javascript/direct.min.js\"></script>"

    def link(self, params=None):
        url = self.checkout_url + '?'
        if params is None:
            params = dict()
        param = urllib.urlencode(params)
        url = url.endswith('?') and (url + param)
        return url

    @classmethod
    def authorize(cls, api, params=None):
        response = cls(api.call('authService', params), api=api)
        return response.response
