from api_request import Api
from util import Util
from twocheckout import Twocheckout


class Sale(Twocheckout):
    def __init__(self, dict_):
        super(self.__class__, self).__init__(dict_)

    @classmethod
    def find(cls, params=None):
        if params is None:
            params = dict()
        response = cls(Api.call('sales/detail_sale', params))
        return response.sale

    @classmethod
    def list(cls, params=None):
        if params is None:
            params = dict()
        response = cls(Api.call('sales/list_sales', params))
        return response.sale_summary

    def refund(self, params=None):
        if params is None:
            params = dict()
        if hasattr(self, 'lineitem_id'):
            params['lineitem_id'] = self.lineitem_id
            url = 'sales/refund_lineitem'
        elif hasattr(self, 'invoice_id'):
            params['invoice_id'] = self.invoice_id
            url = 'sales/refund_invoice'
        else:
            params['sale_id'] = self.sale_id
            url = 'sales/refund_invoice'
        return Sale(Api.call(url, params))

    def stop(self, params=None):
        if params is None:
            params = dict()
        if hasattr(self, 'lineitem_id'):
            params['lineitem_id'] = self.lineitem_id
            return Api.call('sales/stop_lineitem_recurring', params)
        elif hasattr(self, 'sale_id'):
            active_lineitems = Util.active(self)
            if dict(active_lineitems):
                result = dict()
                i = 0
                for k, v in active_lineitems.items():
                    lineitem_id = v
                    params = {'lineitem_id': lineitem_id}
                    result[i] = Api.call('sales/stop_lineitem_recurring', params)
                    i += 1
                response = { "response_code": "OK",
                             "response_message": str(len(result)) + " lineitems stopped successfully"
                }
            else:
                response = {
                    "response_code": "NOTICE",
                    "response_message": "No active recurring lineitems"
                }
        else:
            response = { "response_code": "NOTICE",
                          "response_message": "This method can only be called on a sale or lineitem"
            }
        return Sale(response)

    def active(self):
        active_lineitems = Util.active(self)
        if dict(active_lineitems):
            result = dict()
            i = 0
            for k, v in active_lineitems.items():
                lineitem_id = v
                result[i] = lineitem_id
                i += 1
            response = { "response_code": "ACTIVE",
                         "response_message": str(len(result)) + " active recurring lineitems"
            }
        else:
            response = {
                "response_code": "NOTICE","response_message":
                "No active recurring lineitems"
            }
        return Sale(response)

    def comment(self, params=None):
        if params is None:
            params = dict()
        params['sale_id'] = self.sale_id
        return Sale(Api.call('sales/create_comment', params))

    def ship(self, params=None):
        if params is None:
            params = dict()
        params['sale_id'] = self.sale_id
        return Sale(Api.call('sales/mark_shipped', params))
