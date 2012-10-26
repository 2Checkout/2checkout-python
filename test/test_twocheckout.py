# -*- coding: utf-8 -*-
import os
import sys
import datetime
import unittest
from twocheckout import TwocheckoutError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import twocheckout


NOW = datetime.datetime.now()

EXAMPLE_PRODUCT = {
    'name': 'Example Product',
    'price': 1.00,
}

EXAMPLE_OPTION = {
    'option_name': 'Example Option',
    'option_value_name': 'Test',
    'option_value_surcharge': 1.00,

}

EXAMPLE_COUPON = {
    'date_expire': '2020-12-12',
    'type': 'shipping'
}

EXAMPLE_SALE = {
    'sale_id': 4774380224,
}

EXAMPLE_COMMENT = {
    'sale_comment': "test",
    }

EXAMPLE_REFUND = {
    'comment': "test",
    'category': 1
}

EXAMPLE_SHIP = {
    'tracking_number': 123
}

EXAMPLE_PASSBACK = {
    'sid': '1817037',
    'key': '7AB926D469648F3305AE361D5BD2C3CB',
    'total': '0.01',
    'order_number': '4774380224',
    'secret': 'tango'
}

EXAMPLE_NOTIFICATION = {
    'vendor_id': '1817037',
    'sale_id': '4774380224',
    'invoice_id': '4774380233',
    'md5_hash': '566C45D68B75357AD43F9010CFFE8CF5',
    'secret': 'tango'
}

class TwocheckoutTestCase(unittest.TestCase):
    def setUp(self):
        super(TwocheckoutTestCase, self).setUp()

        twocheckout.Api.credentials({'username':'APIuser1817037', 'password':'APIpass1817037'})

class SaleTest(TwocheckoutTestCase):
    def setUp(self):
        super(SaleTest, self).setUp()

    def test_find_sale(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            self.assertEqual(int(sale.sale_id), 4774380224)
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Unable to find record.")

    def test_list_sale(self):
        params = {'pagesize': 3}
        list = twocheckout.Sale.list(params)
        self.assertEqual(len(list), 3)

    def test_refund_sale(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            result = sale.refund(EXAMPLE_REFUND)
            self.assertEqual(result.message, "refund added to invoice")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Invoice was already refunded.")

    def test_refund_invoice(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            invoice = sale.invoices[0]
            result = invoice.refund(EXAMPLE_REFUND)
            self.assertEqual(result.message, "refund added to invoice")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Invoice was already refunded.")

    def test_refund_lineitem(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            invoice = sale.invoices[0]
            lineitem = invoice.lineitems[0]
            result = lineitem.refund(EXAMPLE_REFUND)
            self.assertEqual(result.message, "lineitem refunded")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Lineitem was already refunded.")

    def test_stop(self):
#        sale stop
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        result = sale.stop()
        self.assertEqual(result.response_message, "No active recurring lineitems")
#        invoice stop
        invoice = sale.invoices[0]
        result = invoice.stop()
        self.assertEqual(result.response_message, "No active recurring lineitems")
#        lineitem stop
        try:
            lineitem = invoice.lineitems[0]
            result = lineitem.stop()
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Lineitem is not scheduled to recur.")

    def test_comment(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        result = sale.comment(EXAMPLE_COMMENT)
        self.assertEqual(result.response_message, "Created comment successfully.")

    def test_ship(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            result = sale.ship(EXAMPLE_SHIP)
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Sale already marked shipped.")

    def test_reauth(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            sale.reauth()
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Payment is already pending or deposited and cannot be reauthorized.")

class ProductTest(TwocheckoutTestCase):
    def setUp(self):
        super(ProductTest, self).setUp()

    def test_crud(self):
#        create
        result = twocheckout.Product.create(EXAMPLE_PRODUCT)
        self.assertEqual(result.response_message, "Product successfully created")
#        find
        EXAMPLE_PRODUCT['product_id'] = result.product_id
        product = twocheckout.Product.find(EXAMPLE_PRODUCT)
        self.assertEqual(product.name, "Example Product")
#        update
        EXAMPLE_PRODUCT['name'] = "Updated Name"
        product = product.update(EXAMPLE_PRODUCT)
        self.assertEqual(product.name, "Updated Name")
#        delete
        result = product.delete(EXAMPLE_PRODUCT)
        self.assertEqual(result.response_message, "Product successfully deleted.")

    def test_list(self):
        params = {'pagesize': 3}
        list = twocheckout.Product.list(params)
        self.assertEqual(len(list), 3)

class OptionTest(TwocheckoutTestCase):
    def setUp(self):
        super(OptionTest, self).setUp()

    def test_crud(self):
#        create
        result = twocheckout.Option.create(EXAMPLE_OPTION)
        self.assertEqual(result.response_message, "Option created successfully")
#        find
        EXAMPLE_OPTION['option_id'] = result.option_id
        option = twocheckout.Option.find(EXAMPLE_OPTION)
        self.assertEqual(option.option_name, "Example Option")
#        update
        params = dict()
        params['option_name'] = "Updated Name"
        params['option_id'] = option.option_id
        params['option_value_id'] = option.option_values[0].option_value_id
        params['option_value_name'] = option.option_values[0].option_value_name
        params['option_value_surcharge'] = option.option_values[0].option_value_surcharge
        option = option.update(params)
        self.assertEqual(option.option_name, "Updated Name")
#        delete
        result = option.delete(EXAMPLE_OPTION)
        self.assertEqual(result.response_message, "Option deleted successfully")

    def test_list(self):
        params = {'pagesize': 3}
        list = twocheckout.Option.list(params)
        self.assertEqual(len(list), 3)

class CouponTest(TwocheckoutTestCase):
    def setUp(self):
        super(CouponTest, self).setUp()

    def test_crud(self):
#        create
        result = twocheckout.Coupon.create(EXAMPLE_COUPON)
        self.assertEqual(result.response_message, "Coupon successfully created")
#        find
        EXAMPLE_COUPON['coupon_code'] = result.coupon_code
        coupon = twocheckout.Coupon.find(EXAMPLE_COUPON)
        self.assertEqual(coupon.coupon_code, result.coupon_code)
#        update
        EXAMPLE_COUPON['date_expire'] = "2020-01-02"
        coupon = coupon.update(EXAMPLE_COUPON)
        self.assertEqual(coupon.date_expire, "2020-01-02")
#        delete
        result = coupon.delete(EXAMPLE_COUPON)
        self.assertEqual(result.response_message, "Coupon successfully deleted.")

class CompanyTest(TwocheckoutTestCase):
    def setUp(self):
        super(CompanyTest, self).setUp()

    def test_retrieve(self):
        company = twocheckout.Company.retrieve()
        self.assertEqual(company.vendor_id, "1817037")

class ContactTest(TwocheckoutTestCase):
    def setUp(self):
        super(ContactTest, self).setUp()

    def test_create(self):
        contact = twocheckout.Contact.retrieve()
        self.assertEqual(contact.vendor_id, "1817037")

class PassbackTest(TwocheckoutTestCase):
    def setUp(self):
        super(PassbackTest, self).setUp()

    def test_check(self):
        params = EXAMPLE_PASSBACK
        result = twocheckout.Passback.check(params)
        self.assertEqual(result.response_code, "SUCCESS")

class NotificationTest(TwocheckoutTestCase):
    def setUp(self):
        super(NotificationTest, self).setUp()

    def test_check(self):
        params = EXAMPLE_NOTIFICATION
        result = twocheckout.Notification.check(params)
        self.assertEqual(result.response_code, "SUCCESS")

if __name__ == '__main__':
    unittest.main()