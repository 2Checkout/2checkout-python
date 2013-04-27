import urllib


class Charge:

    @classmethod
    def form(cls, params=None):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/purchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n"

    @classmethod
    def submit(cls, params=None):
        if params is None:
            params = dict()
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/purchase\" method=\"post\">\n"
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
    def link(cls, params=None, url="https://www.2checkout.com/checkout/purchase?"):
        if params is None:
            params = dict()
        param = urllib.urlencode(params)
        url = url.endswith('?') and (url + param)
        return url
