import urllib


class Charge(object):

    @classmethod
    def _construct_form(cls, params={}):
        form = (
            '<form id="2checkout" '
            'action="https://www.2checkout.com/checkout/purchase" '
            'method="post">'
        )

        for param in params:
            form += '<input type="hidden" name="{0}" value="{1}" />'.format(param, str(params[param]))

        return form + '<input type="submit" value="Proceed to Checkout" /></form>'

    @classmethod
    def form(cls, params={}):
        return cls._construct_form(params=params)

    @classmethod
    def submit(cls, params={}):
        return (
            cls._construct_form(params=params) +
            '<script type="text/javascript">'
            'document.getElementById("2checkout").submit();'
            '</script>'
        )

    @classmethod
    def direct(cls, params={}):
        return (
            cls._construct_form(params=params) +
            '<script src="https://www.2checkout.com/static/checkout/javascript/direct.min.js"></script>'
        )

    @classmethod
    def link(cls, params={}, url="https://www.2checkout.com/checkout/purchase?"):

        if not url.endswith('?'):
            url += '?'

        # add the query string to the url
        url += urllib.urlencode(params)

        return url
