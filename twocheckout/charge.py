import urllib.request, urllib.parse, urllib.error
from .api_request import Api
from .twocheckout import Twocheckout


class Charge(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def form(cls, params=None):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/spurchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n"

    @classmethod
    def submit(cls, params=None):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/spurchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n" + \
               "<script type=\"text/javascript\">document.getElementById('2checkout').submit();</script>"

    @classmethod
    def direct(cls, params=None):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/purchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n" + \
               "<script src=\"https://www.2checkout.com/static/checkout/javascript/direct.min.js\"></script>"

    @classmethod
    def link(cls, params=None, url="https://www.2checkout.com/checkout/spurchase?"):
        if params is None:
            params = dict()
        param = urllib.parse.urlencode(params)
        url = url.endswith('?') and (url + param)
        return url

    @classmethod
    def authorize(cls, params=None):
        response = Charge(Api.call('authService', params))
        return response.response
