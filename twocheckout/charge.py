import urllib


class Charge(object):

    @classmethod
    def form(cls, params={}):
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/purchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n"

    @classmethod
    def submit(cls, params={}):
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/purchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n" + \
               "<script type=\"text/javascript\">document.getElementById('2checkout').submit();</script>"

    @classmethod
    def direct(cls, params={}):
        form = "<form id=\"2checkout\" action=\"https://www.2checkout.com/checkout/purchase\" method=\"post\">\n"
        for param in params:
            form = form + "<input type=\"hidden\" name=\"" + param + "\" value=\"" + str(params[param]) + "\" />\n"
        return form + "<input type=\"submit\" value=\"Proceed to Checkout\" />\n</form>\n" + \
               "<script src=\"https://www.2checkout.com/static/checkout/javascript/direct.min.js\"></script>"

    @classmethod
    def link(cls, params={}, url="https://www.2checkout.com/checkout/purchase?"):
        param = urllib.urlencode(params)
        url = url.endswith('?') and (url + param)
        return url
