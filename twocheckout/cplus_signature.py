import time
import requests
import jwt
import json
from .error import TwocheckoutError


class CplusSignature:
    SIGNATURE_URL = 'https://secure.2checkout.com/checkout/api/encrypt/generate/signature'

    def get_signature(self, merchant_id, buylink_secret_word, json_encoded_convert_plus_parameters, token_expiration=None):
        if not token_expiration:
            token_expiration = 3600
        jwt_token = jwt.encode({
            'sub': merchant_id,
            'iat': str(time.time()).split('.')[0],
            'exp': str(time.time() + token_expiration).split('.')[0]
        }, buylink_secret_word, algorithm='HS512')

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'merchant-token': jwt_token}
        try:
            response = requests.request('POST', self.SIGNATURE_URL, data=json_encoded_convert_plus_parameters,
                                        headers=headers)
        except Exception as e:
            raise TwocheckoutError('REQUEST_FAILED', e.args)

        try:
            signature = json.loads(response.text)
            return signature['signature']
        except Exception as e:
            raise ValueError('Unable to decode server response')
