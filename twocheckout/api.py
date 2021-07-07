import hashlib
import hmac
import codecs
import datetime
import requests
import json
from .error import TwocheckoutError 


class Api:
    api_url = 'https://api.2checkout.com/rest/6.0/'
    resource_url = ''
    merchant_code = None
    secret_key = None

    # endpoint resource
    def set_resource(self, resource):
        self.resource_url = resource + '/'

    def get_resource(self):
        return self.resource_url

    # constructor function used to set the merchant_code & SECRET_KEY
    def __init__(self, params):
        self.merchant_code = str(params['merchant_code'])
        self.secret_key = str(params['secret_key'])

    # set the authentication headers using the VENDOR_ID & SECRET_KEY for creating the hash
    def get_headers(self):
        now = str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        string = str(len(self.merchant_code)) + self.merchant_code + str(len(now)) + now
        string = codecs.encode(string)
        secret_key = codecs.encode(self.secret_key)
        string_hash = hmac.new(secret_key, string, hashlib.md5).hexdigest()
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Avangate-Authentication': 'code="' + self.merchant_code + '" date="' + now + '" hash="' + string_hash + '"'
        }

    # make request to 2Checkout API and returns the response
    # or throws an Error
    def call(self, endpoint, params=None, method='POST'):
        method.upper()
        data_json = json.dumps(params)
        url = self.api_url + endpoint
        try:
            response = requests.request(method, url, data=data_json, headers=self.get_headers())
            return response.text
        except Exception as e:
            raise TwocheckoutError('REQUEST_FAILED', e.args)
