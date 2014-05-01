import urllib
from api_request import Api
from twocheckout import Twocheckout


class Charge(Twocheckout):

    checkout_url = "https://www.2checkout.com/checkout/purchase"

    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def mode(cls, mode):
        if mode == 'sandbox':
            Charge.checkout_url = 'https://sandbox.2checkout.com/checkout/purchase'
        else:
            Charge.checkout_url = 'https://www.2checkout.com/checkout/purchase'

    @classmethod
    def form(cls, params=None, text='Proceed to Checkout'):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"" + Charge.checkout_url + "\" method=\"post\">"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />"
        return form + "<input type=\"submit\" value=\"" + text + "\" /></form>"

    @classmethod
    def submit(cls, params=None, text='Proceed to Checkout'):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"" + Charge.checkout_url + "\" method=\"post\">"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />"
        return form + "<input type=\"submit\" value=\"" + text + "\" /></form>" + \
            "<script type=\"text/javascript\">document.getElementById(\"2checkout\").submit();</script>"

    @classmethod
    def direct(cls, params=None, text='Proceed to Checkout'):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"" + Charge.checkout_url + "\" method=\"post\">"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />"
        return form + "<input type=\"submit\" value=\"" + text + "\" /></form>" + \
            "<script src=\"https://www.2checkout.com/static/checkout/javascript/direct.min.js\"></script>"

    @classmethod
    def link(cls, params=None):
        url = Charge.checkout_url + '?'
        if params is None:
            params = dict()
        param = urllib.urlencode(params)
        url = url.endswith('?') and (url + param)
        return url

    @classmethod
    def authorize(cls, params=None):
        response = Charge(Api.call('authService', params))
        return response.response