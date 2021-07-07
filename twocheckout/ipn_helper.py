import hmac
from .error import TwocheckoutError
from datetime import datetime


# more information on calculating the IPN HASH signature can be found here
# https://knowledgecenter.2checkout.com/API-Integration/Webhooks/06Instant_Payment_Notification_(IPN)/Calculate-the-IPN-HASH-signature#PHP_Hash_Example
class IpnHelper:
    secret_key = None

    def __init__(self, secret):
        self.secret_key = secret

    # check if the received request is a valid one
    def is_valid(self, params):
        if self.secret_key is None:
            raise TwocheckoutError('SECRET KEY MISSING', 'You must pass the secret key to the constructor class')

        try:
            result = ''
            receivedHash = params['HASH']
            for param in params:
                if param != 'HASH':
                    var_type = type(params[param])
                    if var_type is list:
                        result += self.expand(params[param])
                    else:
                        size = str(len(params[param].lstrip()))
                        result += size + params[param].lstrip()
            try:
                calcHash = hmac.new(self.secret_key.encode(), result.encode(), 'md5').hexdigest()
                return receivedHash == calcHash
            except Exception as e:
                raise TwocheckoutError('Hash signatures do not match', e.args)

        except Exception as error:
            raise TwocheckoutError('Exception validating ipn signature', error.args)

    def calculate_ipn_response(self, params):
        try:
            now = datetime.now()
            result = ''
            ipn_response = {'IPN_PID': [params['IPN_PID[]']],
                            'IPN_NAME': [params['IPN_PNAME[]']],
                            'IPN_DATE': params['IPN_DATE'],
                            'DATE': now.strftime('%Y%m%d%H%M%S')}

            for param in ipn_response:
                if type(ipn_response[param]) is list:
                    result += self.expand(ipn_response[param])
                else:
                    size = len(ipn_response[param])
                    result += str(size) + ipn_response[param]

            return '<EPAYMENT>' + ipn_response['DATE'] + '|' + hmac.new(self.secret_key.encode(), result.encode(), 'md5').hexdigest() + '</EPAYMENT>'

        except Exception as e:
            raise TwocheckoutError('Exception generating ipn response', e.args)

    @classmethod
    def expand(cls, val_list):
        result = ''
        for val in val_list:
            size = len(val.lstrip())
            result += str(size) + str(val.lstrip())
        return result
