import urllib.request
import urllib.parse
import urllib.error
import json
from .error import TwocheckoutError


class Api:

    username = None
    password = None
    private_key = None
    seller_id = None
    version = '1'

    @classmethod
    def credentials(cls, credentials):
        Api.username = credentials['username']
        Api.password = credentials['password']

    @classmethod
    def auth_credentials(cls, credentials):
        Api.private_key = credentials['private_key']
        Api.seller_id = credentials['seller_id']

    @classmethod
    def call(cls, method, params=None):
        data = cls.set_opts(method, params)
        url = cls.build_url(method)
        headers = cls.build_headers(method)
        try:
            binary_data = data.encode('ascii')
            req = urllib.request.Request(url, binary_data, headers)
            raw_data = urllib.request.urlopen(req).read()
            try:
                result = raw_data.decode('utf-8')
            except UnicodeDecodeError:
                result = raw_data.decode('utf-8', 'ignore')
            return json.loads(result)
        except urllib.error.HTTPError as e:
            if not hasattr(e, 'read'):
                raise TwocheckoutError(e.code, e.msg)
            else:
                raw_data = e.read()
                result = raw_data.decode('utf-8')
                exception = json.loads(result)
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
            passwd_url = 'https://www.2checkout.com'
            data = urllib.parse.urlencode(params)
            password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            password_manager.add_password(
                None, passwd_url, username, password
            )
            auth_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
            opener = urllib.request.build_opener(auth_handler)
            urllib.request.install_opener(opener)
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
        url = 'https://www.2checkout.com'
        if method == 'authService':
            url += '/checkout/api/' + cls.version + '/' + cls.seller_id + '/rs/' + method
        else:
            url += '/api/' + method
        return url