import hashlib
from .twocheckout import Twocheckout


class Passback(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def check_hash(cls, params={}):
        m = hashlib.md5()

        m.update(params['secret'] + params['sid'] +
                 params['order_number'] + params['total'])

        check_hash = m.hexdigest().upper()

        return check_hash == params['key']

    @classmethod
    def check(cls, params={}):
        if 'order_number' in params and 'total' in params:
            check = Passback.check_hash(params)
            if check:
                response = {
                    "response_code": "SUCCESS",
                    "response_message": "Hash Matched"
                }
            else:
                response = {
                    "response_code": "FAILED",
                    "response_message": "Hash Mismatch"
                }
        else:
            return {
                "response_code": "ERROR",
                "response_message": "You must pass secret word, sid, order_number, total"
            }

        return cls(response)
