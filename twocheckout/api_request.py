import urllib
import urllib2
import json

from error import TwocheckoutError


class Api(object):
    version = '1'

    def __init__(self, seller_id=None, private_key=None, username=None, password=None, mode=None):
        self.seller_id = seller_id
        self.private_key = private_key
        self.username = username
        self.password = password
        self.mode = mode

    def credentials(self, credentials):
        self.username = credentials['username']
        self.password = credentials['password']
        if 'mode' in credentials:
            self.mode = credentials['mode']

    def auth_credentials(self, credentials):
        self.private_key = credentials['private_key']
        self.seller_id = credentials['seller_id']
        if 'mode' in credentials:
            self.mode = credentials['mode']

    def call(self, method, params=None):
        data = self.set_opts(method, params)
        url = self.build_url(method)
        headers = self.build_headers(method)
        try:
            req = urllib2.Request(url, data, headers)
            result = urllib2.urlopen(req).read()
            result_safe = None
            try:
                result_safe = unicode(result)
            except UnicodeDecodeError:
                result_safe = unicode(str(result).decode('utf-8', 'ignore'))
            return json.loads(result_safe)
        except urllib2.HTTPError, e:
            if not hasattr(e, 'read'):
                raise TwocheckoutError(e.code, e.msg)
            else:
                exception = json.loads(e.read())
                if method == 'authService':
                    raise TwocheckoutError(exception['exception']['errorCode'], exception['exception']['errorMsg'])
                else:
                    raise TwocheckoutError(exception['errors'][0]['code'], exception['errors'][0]['message'])

    def set_opts(self, method, params=None):
        if method == 'authService':
            params['sellerId'] = self.seller_id
            params['privateKey'] = self.private_key
            data = json.dumps(params)
        else:
            username = self.username
            password = self.password
            if self.mode == 'sandbox':
                passwd_url = 'https://sandbox.2checkout.com'
            else:
                passwd_url = 'https://www.2checkout.com'
            data = urllib.urlencode(params)
            password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
            password_manager.add_password(
                None, passwd_url, username, password
            )
            auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
            opener = urllib2.build_opener(auth_handler)
            urllib2.install_opener(opener)
        return data

    def build_headers(self, method):
        if method == 'authService':
            headers = {
                'Accept': 'application/json',
                'User-Agent': '2Checkout Python/0.1.0/%s',
                'Content-Type': 'application/JSON'
            }
        else:
            headers = {
                'Accept': 'application/json',
                'User-Agent': '2Checkout Python/0.1.0/%s'
            }
        return headers

    def build_url(self, method):
        if self.mode == 'sandbox':
            url = 'https://sandbox.2checkout.com'
        else:
            url = 'https://www.2checkout.com'
        if method == 'authService':
            url += '/checkout/api/' + self.version + '/' + self.seller_id + '/rs/' + method
        else:
            url += '/api/' + method
        return url
