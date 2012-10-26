class Util:

    @classmethod
    def active(cls, sale):
        i = 0
        if hasattr(sale, 'recurring'):
            invoice = sale
        else:
            invoices = dict()
            sale = sale.invoices
            for invoice in sale:
                invoices[i] = invoice
                i += 1
            invoice = max(invoices.values())
        i = 0
        lineitems = dict()
        for lineitem_id in invoice.lineitems:
            if lineitem_id.billing.recurring_status == 'active':
                lineitems[i] = lineitem_id['lineitem_id']
                i += 1
        return lineitems