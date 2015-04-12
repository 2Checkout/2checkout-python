from util import Util
from twocheckout import Twocheckout


class Sale(Twocheckout):
    @classmethod
    def find(cls, api, params=None):
        if params is None:
            params = dict()
        response = cls(api.call('sales/detail_sale', params), api=api)
        return response.sale

    @classmethod
    def list(cls, api, params=None):
        if params is None:
            params = dict()
        response = cls(api.call('sales/list_sales', params), api=api)
        return response.sale_summary

    def refund(self, params=None):
        api = self.api
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
        return Sale(api.call(url, params), api=api)

    def stop(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        if hasattr(self, 'lineitem_id'):
            params['lineitem_id'] = self.lineitem_id
            return api.call('sales/stop_lineitem_recurring', params)
        elif hasattr(self, 'sale_id'):
            active_lineitems = Util.active(self)
            if dict(active_lineitems):
                result = dict()
                i = 0
                for k, v in active_lineitems.items():
                    lineitem_id = v
                    params = {'lineitem_id': lineitem_id}
                    result[i] = api.call('sales/stop_lineitem_recurring', params)
                    i += 1
                response = {
                    "response_code": "OK",
                    "response_message": str(len(result)) + " lineitems stopped successfully"
                }
            else:
                response = {
                    "response_code": "NOTICE",
                    "response_message": "No active recurring lineitems"
                }
        else:
            response = {
                "response_code": "NOTICE",
                "response_message": "This method can only be called on a sale or lineitem"
            }
        return Sale(response, api=api)

    def active(self):
        api = self.api
        active_lineitems = Util.active(self)
        if dict(active_lineitems):
            result = dict()
            i = 0
            for k, v in active_lineitems.items():
                lineitem_id = v
                result[i] = lineitem_id
                i += 1
            response = {
                "response_code": "ACTIVE",
                "response_message": str(len(result)) + " active recurring lineitems"
            }
        else:
            response = {
                "response_code": "NOTICE",
                "response_message": "No active recurring lineitems"
            }
        return Sale(response, api=api)

    def comment(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['sale_id'] = self.sale_id
        return Sale(api.call('sales/create_comment', params), api=api)

    def ship(self, params=None):
        api = self.api
        if params is None:
            params = dict()
        params['sale_id'] = self.sale_id
        return Sale(api.call('sales/mark_shipped', params), api=api)

    def reauth(self):
        api = self.api
        params = dict()
        params['sale_id'] = self.sale_id
        return Sale(api.call('sales/reauth', params), api=api)
