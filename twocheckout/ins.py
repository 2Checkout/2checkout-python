import hashlib
from twocheckout import Twocheckout

class Notification(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def check_hash(cls, params=None):
        m = hashlib.md5()
        m.update(params['sale_id'])
        m.update(params['vendor_id'])
        m.update(params['invoice_id'])
        m.update(params['secret'])
        check_hash = m.hexdigest()
        check_hash = check_hash.upper()
        if check_hash == params['md5_hash']:
            return True
        else:
            return False

    @classmethod
    def check(cls, params=None):
        if params is None:
            params = dict()
        if 'sale_id' in params and 'invoice_id' in params:
            check = Notification.check_hash(params)
            if check:
                response = { "response_code": "SUCCESS",
                             "response_message": "Hash Matched"
                }
            else:
                response =  { "response_code": "FAILED",
                              "response_message": "Hash Mismatch"
                }
        else:
            response = { "response_code": "ERROR",
                         "response_message": "You must pass sale_id, vendor_id, invoice_id, secret word."
            }
        return cls(response)