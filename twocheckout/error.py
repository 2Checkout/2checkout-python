class TwocheckoutError(Exception):
    def __init__(self, code=None, msg=None):
        super(TwocheckoutError, self).__init__(msg)
        self.code = code
        self.msg = msg
