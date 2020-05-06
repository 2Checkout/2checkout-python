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
    'name': 'Python Example Product',
    'price': 2.00
}

EXAMPLE_SALE = {
    'sale_id': 250353589267
}

EXAMPLE_COMMENT = {
    'sale_comment': "python3 test"
}

EXAMPLE_REFUND = {
    'comment': "Python Refund Sale",
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
    "sellerId": "CREDENTIALS_HERE",
    "privateKey": "CREDENTIALS_HERE",
    "merchantOrderId": "123",
    "token": "CUSTOMER-CLIENT-SIDE-TOKEN",
    "currency": "USD",
    "total": "2.00",
    "demo": True,
     "billingAddr": {
        "name": "John Doe",
        "addrLine1": "123 Test St",
        "city": "Columbus",
        "state": "Ohio",
        "zipCode": "43123",
        "country": "USA",
        "email": "example@2co.com",
        "phoneNumber": "5555555555"
    }
}

class TwocheckoutTestCase(unittest.TestCase):
    def setUp(self):
        super(TwocheckoutTestCase, self).setUp()

        twocheckout.Api.credentials({
            'username': 'CREDENTIALS_HERE',
            'password': 'CREDENTIALS_HERE'
        })

        twocheckout.Api.auth_credentials({
            'private_key': 'CREDENTIALS_HERE',
            'seller_id': 'CREDENTIALS_HERE'
        })


class AuthorizationTest(TwocheckoutTestCase):
    def setUp(self):
        super(AuthorizationTest, self).setUp()

## Place order test
    def test_1_auth(self):
        params = EXAMPLE_AUTH
        try:
            result = twocheckout.Charge.authorize(params)

            ## use OrderNumber for sale_id for next tests
            print("OrderNumber: ", result.orderNumber)
            self.assertEqual(result.responseCode, "APPROVED")
        except TwocheckoutError as error:
            self.assertEqual(error.msg, "Unauthorized")

class SaleTest(TwocheckoutTestCase):
    def setUp(self):
        super(SaleTest, self).setUp()

    def test_1_find_sale(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            self.assertEqual(int(sale.sale_id), 250353589267)
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
            self.assertEqual(error.message, "Amount greater than remaining balance on invoice.")

## If you have already run test_3 then test_4 will fail for the same sale_id.
    def test_4_refund_invoice(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            invoice = sale.invoices[0]
            result = invoice.refund(EXAMPLE_REFUND)
            self.assertEqual(result.response_message, "refund added to invoice")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Amount greater than remaining balance on invoice.")

    def test_5_refund_lineitem(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            invoice = sale.invoices[0]
            lineitem = invoice.lineitems[0]
            result = lineitem.refund(EXAMPLE_REFUND)
            self.assertEqual(result.response_message, "lineitem refunded")
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Lineitem amount greater than remaining balance on invoice.")

    def test_6_stop_sale(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        result = sale.stop()
        self.assertEqual(result.response_message, "No active recurring lineitems")

    def test_7_stop_invoice(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        invoice = sale.invoices[0]
        result = invoice.stop()
        self.assertEqual(result.response_message, "No active recurring lineitems")

## If you have already run "test_7_stop_invoice" then "test_8_stop_sale_lineitem" will fail for the same sale_id.
    def test_8_stop_sale_lineitem(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        invoice = sale.invoices[0]
        try:
            lineitem = invoice.lineitems[0]
            result = lineitem.stop()
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Lineitem is not scheduled to recur.")

    def test_9_comment(self):
        sale = twocheckout.Sale.find(EXAMPLE_SALE)
        result = sale.comment(EXAMPLE_COMMENT)
        self.assertEqual(result.response_message, "Created comment successfully.")

    def test_10_ship(self):
        try:
            sale = twocheckout.Sale.find(EXAMPLE_SALE)
            result = sale.ship(EXAMPLE_SHIP)
        except TwocheckoutError as error:
            self.assertEqual(error.message, "Sale already marked shipped.")

class ProductTest(TwocheckoutTestCase):
    def setUp(self):
        super(ProductTest, self).setUp()

    def test_1_create(self):
        result = twocheckout.Product.create(EXAMPLE_PRODUCT)
        self.assertEqual(result.response_message, "Product successfully created.")
        EXAMPLE_PRODUCT['product_id'] = result.product_id

    def test_2_find(self):
        product = twocheckout.Product.find(EXAMPLE_PRODUCT)
        self.assertEqual(product.name, "Python Example Product")

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

class CompanyTest(TwocheckoutTestCase):
    def setUp(self):
        super(CompanyTest, self).setUp()

    def test_1_retrieve(self):
        company = twocheckout.Company.retrieve()
        self.assertEqual(company.vendor_id, "250111206876")

class ContactTest(TwocheckoutTestCase):
    def setUp(self):
        super(ContactTest, self).setUp()

    def test_1_create(self):
        contact = twocheckout.Contact.retrieve()
        self.assertEqual(contact.vendor_id, "250111206876")

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

if __name__ == '__main__':
    unittest.main()
