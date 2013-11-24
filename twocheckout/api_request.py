import urllib
import urllib2
import json
from error import TwocheckoutError


class Api(object):

    username = None
    password = None

    @classmethod
    def credentials(cls, credentials):
        cls.username = credentials['username']
        cls.password = credentials['password']

    @classmethod
    def call(cls, method, params={}):
        headers = {'Accept': 'application/json',
                   'User-Agent': '2Checkout Python/0.1.0/%s'
        }
        base_url = 'https://www.2checkout.com/api/'
        url = base_url + method
        data = urllib.urlencode(params)
        password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_manager.add_password(
            None, 'https://www.2checkout.com', cls.username, cls.password
        )
        auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        try:
            req = urllib2.Request(url, data, headers)
            result = urllib2.urlopen(req).read()
            return json.loads(result)
        except urllib2.HTTPError, e:
            exception = json.loads(e.read())
            raise TwocheckoutError(exception['errors'][0]['code'], exception['errors'][0]['message'])
