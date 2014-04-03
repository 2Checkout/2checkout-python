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
    'price': 1.00
}

EXAMPLE_OPTION = {
    'option_name': 'Example Option',
    'option_value_name': 'Test',
    'option_value_surcharge': 1.00
}

EXAMPLE_COUPON = {
    'date_expire': '2020-12-12',
    'type': 'shipping'
}

EXAMPLE_SALE = {
    'sale_id': 9093717691800
}

EXAMPLE_COMMENT = {
    'sale_comment': "test"
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

EXAMPLE_AUTH = {
    'merchantOrderId': '123',
    'token': 'NTQyZTQyOTMtNjA0Ni00NzM4LTkyNDItNjVlMmUzZTU2NTNj',
    'currency': 'USD',
    'total': '1.00',
    'billingAddr': {
        'name': 'Testing Tester',
        'addrLine1': '123 Test St',
        'city': 'Columbus',
        'state': 'OH',
        'zipCode': '43123',
        'country': 'USA',
        'email': 'cchristenson@2co.com',
        'phoneNumber': '555-555-5555'
    }
}

class TwocheckoutTestCase(unittest.TestCase):
    def setUp(self):
        super(TwocheckoutTestCase, self).setUp()

        twocheckout.Api.credentials({
            'username': 'testlibraryapi901248204',
            'password': 'testlibraryapi901248204PASS',
            'mode': 'sandbox'
        })

        twocheckout.Api.auth_credentials({
            'private_key': 'BE632CB0-BB29-11E3-AFB6-D99C28100996',
            'seller_id': '901248204',
            'mode': 'sandbox'
        })

class SaleTest(TwocheckoutTestCase):
    def setUp(self):
        super(SaleTest, self).setUp()

    def test_1_find_sale(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            self.assertEqual(int(sale.sale_id), 9093717691800)
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Unable to find record.")

    def test_2_list_sale(self):
        params = {'pagesize': 2}
        list = twocheckout.Sale.list(params)
        self.assertEqual(len(list), 2)

    def test_3_refund_sale(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            result = sale.refund(EXAMPLE_REFUND)
            self.assertEqual(result.message, "refund added to invoice")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Invoice was already refunded.")

    def test_4_refund_invoice(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            invoice = sale.invoices[0]
            result = invoice.refund(EXAMPLE_REFUND)
            self.assertEqual(result.message, "refund added to invoice")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Invoice was already refunded.")

    def test_5_refund_lineitem(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            invoice = sale.invoices[0]
            lineitem = invoice.lineitems[0]
            result = lineitem.refund(EXAMPLE_REFUND)
            self.assertEqual(result.message, "lineitem refunded")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Lineitem was already refunded.")

    def test_6_stop_sale(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        result = sale.stop()
        self.assertEqual(result.response_message, "No active recurring lineitems")

    def test_7_stop_invoice(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        invoice = sale.invoices[0]
        result = invoice.stop()
        self.assertEqual(result.response_message, "No active recurring lineitems")

    def test_6_stop_sale(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        invoice = sale.invoices[0]
        try:
            lineitem = invoice.lineitems[0]
            result = lineitem.stop()
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Lineitem is not scheduled to recur.")

    def test_7_comment(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        result = sale.comment(EXAMPLE_COMMENT)
        self.assertEqual(result.response_message, "Created comment successfully.")

    def test_8_ship(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            result = sale.ship(EXAMPLE_SHIP)
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Sale already marked shipped.")

    def test_9_reauth(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            sale.reauth()
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Payment is already pending or deposited and cannot be reauthorized.")

class ProductTest(TwocheckoutTestCase):
    def setUp(self):
        super(ProductTest, self).setUp()

    def test_1_create(self):
        result = twocheckout.Product.create(EXAMPLE_PRODUCT)
        self.assertEqual(result.response_message, "Product successfully created")
        EXAMPLE_PRODUCT['product_id'] = result.product_id

    def test_2_find(self):
        product = twocheckout.Product.find(EXAMPLE_PRODUCT)
        self.assertEqual(product.name, "Example Product")

    def test_3_update(self):
        product = twocheckout.Product.find(EXAMPLE_PRODUCT)
        EXAMPLE_PRODUCT['name'] = "Updated Name"
        product = product.update(EXAMPLE_PRODUCT)
        self.assertEqual(product.name, "Updated Name")

    def test_4_delete(self):
        product = twocheckout.Product.find(EXAMPLE_PRODUCT)
        result = product.delete(EXAMPLE_PRODUCT)
        self.assertEqual(result.response_message, "Product successfully deleted.")

    def test_5_list(self):
        params = {'pagesize': 2}
        list = twocheckout.Product.list(params)
        self.assertEqual(len(list), 2)

class OptionTest(TwocheckoutTestCase):
    def setUp(self):
        super(OptionTest, self).setUp()

    def test_1_create(self):
        result = twocheckout.Option.create(EXAMPLE_OPTION)
        self.assertEqual(result.response_message, "Option created successfully")
        EXAMPLE_OPTION['option_id'] = result.option_id

    def test_2_find(self):
        option = twocheckout.Option.find(EXAMPLE_OPTION)
        self.assertEqual(option.option_name, "Example Option")

    def test_3_update(self):
        option = twocheckout.Option.find(EXAMPLE_OPTION)
        params = dict()
        params['option_name'] = "Updated Name"
        option = option.update(params)
        self.assertEqual(option.option_name, "Updated Name")

    def test_4_delete(self):
        option = twocheckout.Option.find(EXAMPLE_OPTION)
        result = option.delete(EXAMPLE_OPTION)
        self.assertEqual(result.response_message, "Option deleted successfully")

    def test_5_list(self):
        params = {'pagesize': 3}
        list = twocheckout.Option.list(params)
        self.assertEqual(len(list), 3)

class CouponTest(TwocheckoutTestCase):
    def setUp(self):
        super(CouponTest, self).setUp()

    def test_1_create(self):
        result = twocheckout.Coupon.create(EXAMPLE_COUPON)
        EXAMPLE_COUPON['coupon_code'] = result.coupon_code
        self.assertEqual(result.response_message, "Coupon successfully created")

    def test_2_find(self):
        coupon = twocheckout.Coupon.find(EXAMPLE_COUPON)
        self.assertEqual(coupon.coupon_code, EXAMPLE_COUPON['coupon_code'])

    def test_3_update(self):
        coupon = twocheckout.Coupon.find(EXAMPLE_COUPON)
        EXAMPLE_COUPON['date_expire'] = "2020-01-02"
        coupon = coupon.update(EXAMPLE_COUPON)
        self.assertEqual(coupon.date_expire, "2020-01-02")

    def test_4_delete(self):
        coupon = twocheckout.Coupon.find(EXAMPLE_COUPON)
        result = coupon.delete(EXAMPLE_COUPON)
        self.assertEqual(result.response_message, "Coupon successfully deleted.")

class CompanyTest(TwocheckoutTestCase):
    def setUp(self):
        super(CompanyTest, self).setUp()

    def test_1_retrieve(self):
        company = twocheckout.Company.retrieve()
        self.assertEqual(company.vendor_id, "901248204")

class ContactTest(TwocheckoutTestCase):
    def setUp(self):
        super(ContactTest, self).setUp()

    def test_1_create(self):
        contact = twocheckout.Contact.retrieve()
        self.assertEqual(contact.vendor_id, "901248204")

class PaymentTest(TwocheckoutTestCase):
    def setUp(self):
        super(PaymentTest, self).setUp()

    def test_1_pending(self):
        payment = twocheckout.Payment.pending()
        self.assertEqual(payment.release_level, "300")

    def test_2_list(self):
        payments = twocheckout.Payment.list()
        self.assertEqual(len(payments), 0)

class PassbackTest(TwocheckoutTestCase):
    def setUp(self):
        super(PassbackTest, self).setUp()

    def test_1_check(self):
        params = EXAMPLE_PASSBACK
        result = twocheckout.Passback.check(params)
        self.assertEqual(result.response_code, "SUCCESS")

class NotificationTest(TwocheckoutTestCase):
    def setUp(self):
        super(NotificationTest, self).setUp()

    def test_1_check(self):
        params = EXAMPLE_NOTIFICATION
        result = twocheckout.Notification.check(params)
        self.assertEqual(result.response_code, "SUCCESS")

class AuthorizationTest(TwocheckoutTestCase):
    def setUp(self):
        super(AuthorizationTest, self).setUp()

    def test_1_auth(self):
        params = EXAMPLE_AUTH
        try:
            result = twocheckout.Charge.authorize(params)
            self.assertEqual(result.responseCode, "APPROVED")
        except TwocheckoutError as error:
            self.assertEqual(error.msg, "Unauthorized")

if __name__ == '__main__':
    unittest.main()
