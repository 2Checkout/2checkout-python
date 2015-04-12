class Twocheckout(dict):
    def __init__(self, dict_, api=None):
        super(Twocheckout, self).__init__(dict_)
        self.api = api
        for key in self:
            item = self[key]
            if isinstance(item, list):
                for id, it in enumerate(item):
                    if isinstance(it, dict):
                        item[id] = self.__class__(it, api=api)
            elif isinstance(item, dict):
                self[key] = self.__class__(item, api=api)

    def __getattr__(self, key):
        return self[key]
