import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import json
from .error import TwocheckoutError


class Api:

    username = []
    password = []

    @classmethod
    def credentials(cls, credentials):
        Api.username = credentials['username']
        Api.password = credentials['password']

    @classmethod
    def call(cls, method, params=None):
        username = cls.username
        password = cls.password
        headers = {'Accept': 'application/json',
                   'User-Agent': '2Checkout Python/0.1.0/%s'
        }
        base_url = 'https://www.2checkout.com/api/'
        url = base_url + method
        data = urllib.parse.urlencode(params)
        password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_manager.add_password(
            None, 'https://www.2checkout.com', username, password
        )
        auth_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
        opener = urllib.request.build_opener(auth_handler)
        urllib.request.install_opener(opener)
        try:
            binary_data = data.encode('ascii')
            req = urllib.request.Request(url, binary_data, headers)
            raw_data = urllib.request.urlopen(req).read()
            result = raw_data.decode('utf-8')
            return json.loads(result)
        except urllib.error.HTTPError as e:
            raw_data = e.read()
            result = raw_data.decode('utf-8')
            exception = json.loads(result)
            raise TwocheckoutError(exception['errors'][0]['code'], exception['errors'][0]['message'])
