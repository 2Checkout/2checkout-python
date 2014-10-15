import urllib
import urllib2
import json
from error import TwocheckoutError


class Api:

    username = None
    password = None
    private_key = None
    seller_id = None
    mode = None
    version = '1'

    @classmethod
    def credentials(cls, credentials):
        Api.username = credentials['username']
        Api.password = credentials['password']
        if 'mode' in credentials:
            Api.mode = credentials['mode']

    @classmethod
    def auth_credentials(cls, credentials):
        Api.private_key = credentials['private_key']
        Api.seller_id = credentials['seller_id']
        if 'mode' in credentials:
            Api.mode = credentials['mode']

    @classmethod
    def call(cls, method, params=None):
        data = cls.set_opts(method, params)
        url = cls.build_url(method)
        headers = cls.build_headers(method)
        try:
            req = urllib2.Request(url, data, headers)
            result = urllib2.urlopen(req).read()
            result_safe=None
            try:
                result_safe = unicode(result)
            except UnicodeDecodeError:
                result_safe = unicode( str(result).decode('utf-8', 'ignore') )
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

    @classmethod
    def set_opts(cls, method, params=None):
        if method == 'authService':
            params['sellerId'] = cls.seller_id
            params['privateKey'] = cls.private_key
            data = json.dumps(params)
        else:
            username = cls.username
            password = cls.password
            if cls.mode == 'sandbox':
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

    @classmethod
    def build_headers(cls, method):
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

    @classmethod
    def build_url(cls, method):
        if cls.mode == 'sandbox':
            url = 'https://sandbox.2checkout.com'
        else:
            url = 'https://www.2checkout.com'
        if method == 'authService':
            url += '/checkout/api/' + cls.version + '/' + cls.seller_id + '/rs/' + method
        else:
            url += '/api/' + method
        return url
