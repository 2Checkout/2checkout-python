# -*- coding: utf-8 -*-
import os
import sys
import datetime
import unittest
import twocheckout
from test import config
import hmac

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

NOW = datetime.datetime.now()

auth_params = {
    'merchant_code': config.TWOCHECKOUT_TEST_MERCHANT_ID,
    'secret_key': config.TWOCHECKOUT_TEST_MERCHANT_SECRET_KEY,
}
order_transaction_id = '147288494'
order_get_test = {"meta": {"status": "success", "message": "ok"},
                  "body": {'RefNo': '147288494', 'OrderNo': 0, 'ExternalReference': 'REST_API_AVANGTE',
                           'ShopperRefNo': None,
                           'Status': 'PENDING', 'ApproveStatus': 'WAITING', 'VendorApproveStatus': 'OK',
                           'MerchantCode': config.TWOCHECKOUT_TEST_MERCHANT_ID, 'Language': 'en',
                           'OrderDate': '2021-03-19 11:49:50',
                           'FinishDate': None,
                           'Source': 'testAPI.com',
                           'Affiliate': {'AffiliateCode': None, 'AffiliateSource': None, 'AffiliateName': None,
                                         'AffiliateUrl': None},
                           'HasShipping': False,
                           'BillingDetails': {'FiscalCode': None, 'TaxOffice': None, 'Phone': None,
                                              'FirstName': 'Customer',
                                              'LastName': '2Checkout', 'Company': None,
                                              'Email': 'testcustomer@2Checkout.com',
                                              'Address1': 'Test Address', 'Address2': None, 'City': 'LA',
                                              'Zip': '12345',
                                              'CountryCode': 'us', 'State': 'California'},
                           'DeliveryDetails': {'Phone': None, 'FirstName': 'Customer', 'LastName': '2Checkout',
                                               'Company': None,
                                               'Email': 'testcustomer@2Checkout.com', 'Address1': 'Test Address',
                                               'Address2': None,
                                               'City': 'LA', 'Zip': '12345', 'CountryCode': 'us',
                                               'State': 'California'},
                           'PaymentDetails': {'Type': 'CC', 'Currency': 'usd',
                                              'PaymentMethod': {'Authorize3DS': None, 'Vendor3DSReturnURL': None,
                                                                'Vendor3DSCancelURL': None, 'FirstDigits': '4111',
                                                                'LastDigits': '1111', 'CardType': 'Visa',
                                                                'RecurringEnabled': True},
                                              'CustomerIP': '91.220.121.21'}, 'DeliveryInformation': {
                          'ShippingMethod': {'Code': None, 'TrackingUrl': None, 'TrackingNumber': None,
                                             'Comment': None}},
                           'CustomerDetails': None, 'Origin': 'API', 'AvangateCommission': 4.1, 'OrderFlow': 'REGULAR',
                           'GiftDetails': None, 'PODetails': None, 'ExtraInformation': None, 'PartnerCode': None,
                           'PartnerMargin': None, 'PartnerMarginPercent': None, 'ExtraMargin': None,
                           'ExtraMarginPercent': None,
                           'ExtraDiscount': None, 'ExtraDiscountPercent': None, 'LocalTime': None, 'TestOrder': False,
                           'FxRate': 1,
                           'FxMarkup': 0, 'PayoutCurrency': 'USD', 'DeliveryFinalized': False, 'Errors': None,
                           'Items': [{
                               'ProductDetails': {
                                   'Name': 'Dynamic product',
                                   'ShortDescription': 'Test description',
                                   'Tangible': False,
                                   'IsDynamic': True,
                                   'ExtraInfo': None,
                                   'RenewalStatus': False,
                                   'Subscriptions': None,
                                   'DeliveryInformation': {
                                       'Delivery': 'NO_DELIVERY',
                                       'DownloadFile': None,
                                       'DeliveryDescription': '',
                                       'CodesDescription': '',
                                       'Codes': []}},
                               'PriceOptions': [
                                   {
                                       'Code': 'OPT1_292',
                                       'Name': 'OPT1',
                                       'Required': True,
                                       'Options': [
                                           {
                                               'Name': 'Name LR',
                                               'Value': 'f7f4d3d5546e4f25e8dcdaf8301c34d6',
                                               'Surcharge': '7.00'}]}],
                               'Price': {
                                   'UnitNetPrice': 107,
                                   'UnitGrossPrice': 107,
                                   'UnitVAT': 0,
                                   'UnitDiscount': 0,
                                   'UnitNetDiscountedPrice': 107,
                                   'UnitGrossDiscountedPrice': 107,
                                   'UnitAffiliateCommission': 0,
                                   'ItemUnitNetPrice': 0,
                                   'ItemUnitGrossPrice': 0,
                                   'ItemNetPrice': 0,
                                   'ItemGrossPrice': 0,
                                   'VATPercent': 0,
                                   'HandlingFeeNetPrice': 0,
                                   'HandlingFeeGrossPrice': 0,
                                   'Currency': 'usd',
                                   'NetPrice': 107,
                                   'GrossPrice': 107,
                                   'NetDiscountedPrice': 107,
                                   'GrossDiscountedPrice': 107,
                                   'Discount': 0,
                                   'VAT': 0,
                                   'AffiliateCommission': 0},
                               'LineItemReference': '69057567c67d17d570523b4ea67fe8770fdbc5bd',
                               'PurchaseType': 'PRODUCT',
                               'ExternalReference': '',
                               'Quantity': 1,
                               'SKU': None,
                               'CrossSell': None,
                               'Trial': None,
                               'AdditionalFields': None,
                               'Promotion': None,
                               'RecurringOptions': None,
                               'SubscriptionStartDate': None,
                               'SubscriptionCustomSettings': None}],
                           'Promotions': [], 'AdditionalFields': None, 'Currency': 'usd', 'NetPrice': 107,
                           'GrossPrice': 107,
                           'NetDiscountedPrice': 107, 'GrossDiscountedPrice': 107, 'Discount': 0, 'VAT': 0,
                           'AffiliateCommission': 0,
                           'CustomParameters': None
                           }}
order_params_test = {
    "Country": "us",
    "Currency": "USD",
    "CustomerIP": "91.220.121.21",
    "ExternalReference": "REST_API_AVANGTE",
    "Language": "en",
    "Source": "testAPI.com",
    "BillingDetails": {
        "Address1": "Test Address",
        "City": "LA",
        "State": "California",
        "CountryCode": "US",
        "Email": "testcustomer@2Checkout.com",
        "FirstName": "Customer",
        "LastName": "2Checkout",
        "Zip": "12345"
    },
    "Items": [
        {
            "Name": "Dynamic product",
            "Description": "Test description",
            "Quantity": 1,
            "IsDynamic": True,
            "Tangible": False,
            "PurchaseType": "PRODUCT",
            "CrossSell": {
                "CampaignCode": "CAMPAIGN_CODE",
                "ParentCode": "MASTER_PRODUCT_CODE"
            },
            "Price": {
                "Amount": 100,
                "Type": "CUSTOM"
            },
            "PriceOptions": [
                {
                    "Name": "OPT1",
                    "Options": [
                        {
                            "Name": "Name LR",
                            "Value": "Value LR",
                            "Surcharge": 7
                        }
                    ]
                }
            ],
            "RecurringOptions": {
                "CycleLength": 2,
                "CycleUnit": "DAY",
                "CycleAmount": 12.2,
                "ContractLength": 3,
                "ContractUnit": "DAY"
            }
        }
    ],
    "PaymentDetails": {
        "Type": "CC",
        "Currency": "USD",
        "CustomerIP": "91.220.121.21",
        "PaymentMethod": {
            "CardNumber": "4111111111111111",
            "CardType": "VISA",
            "Vendor3DSReturnURL": "www.success.com",
            "Vendor3DSCancelURL": "www.fail.com",
            "ExpirationYear": "2044",
            "ExpirationMonth": "12",
            "CCID": "123",
            "HolderName": "John Doe",
            "RecurringEnabled": True,
            "HolderNameTime": 1,
            "CardNumberTime": 1
        }
    }
}
json_encoded_convert_plus_parameters = '{"merchant":"' \
                                       + config.TWOCHECKOUT_TEST_MERCHANT_ID \
                                       + '","dynamic":1,"src":"DJANGO",' \
                                         '"return-url":"https:\/\/google.com",' \
                                         '"return-type":"redirect",' \
                                         '"expiration":1617189603,"order-ext-ref":292,' \
                                         '"customer-ext-ref":"example@example.com",' \
                                         '"currency":"GBP","test":"1","language":"en",' \
                                         '"prod":"test site","price":"71.03","qty":"1",' \
                                         '"type":"PRODUCT","tangible":"0",' \
                                         '"ship-name":"John Doe","ship-country":"US",' \
                                         '"ship-state":"AL",' \
                                         '"ship-email":"example@example.com",' \
                                         '"ship-address":"Example","ship-address2":"",' \
                                         '"ship-city":"Example","name":"John Doe",' \
                                         '"phone":"756852919","country":"US","state":"AL",' \
                                         '"email":"example@example.com",' \
                                         '"address":"Example","address2":"",' \
                                         '"city":"Example","zip":"35242","company-name":""} '

ipn_payload = {
    'GIFT_ORDER': '0',
    'SALEDATE': '2021-04-08 16:29:38',
    'PAYMENTDATE': '2021-04-08 16:29:42',
    'REFNO': '148998082',
    'REFNOEXT': 'REST_API_AVANGTE',
    'SHOPPER_REFERENCE_NUMBER': '',
    'ORDERNO': '8978',
    'ORDERSTATUS': 'COMPLETE',
    'PAYMETHOD': 'Visa/MasterCard',
    'PAYMETHOD_CODE': 'CCVISAMC',
    'FIRSTNAME': 'Customer',
    'LASTNAME': '2Checkout',
    'COMPANY': '',
    'REGISTRATIONNUMBER': '',
    'FISCALCODE': '',
    'TAX_OFFICE': '',
    'CBANKNAME': '',
    'CBANKACCOUNT': '',
    'ADDRESS1': 'Test Address',
    'ADDRESS2': '',
    'CITY': 'LA',
    'STATE': 'California',
    'ZIPCODE': '12345',
    'COUNTRY': 'United States of America',
    'COUNTRY_CODE': 'us',
    'PHONE': '',
    'FAX': '',
    'CUSTOMEREMAIL': 'testcustomer@2Checkout.com',
    'FIRSTNAME_D': 'Customer',
    'LASTNAME_D': '2Checkout',
    'COMPANY_D': '',
    'ADDRESS1_D': 'Test Address',
    'ADDRESS2_D': '',
    'CITY_D': 'LA',
    'STATE_D': 'California',
    'ZIPCODE_D': '12345',
    'COUNTRY_D': 'United States of America',
    'COUNTRY_D_CODE': 'us',
    'PHONE_D': '',
    'EMAIL_D': 'testcustomer@2Checkout.com',
    'IPADDRESS': '91.220.121.21',
    'IPCOUNTRY': 'Romania',
    'COMPLETE_DATE': '2021-04-08 16:29:48',
    'TIMEZONE_OFFSET': 'GMT+03:00',
    'CURRENCY': 'USD',
    'LANGUAGE': 'en',
    'ORDERFLOW': 'REGULAR',
    'IPN_PID[]': '35144095',
    'IPN_PNAME[]': 'Dynamic product',
    'IPN_PCODE[]': '',
    'IPN_EXTERNAL_REFERENCE[]': '',
    'IPN_INFO[]': '',
    'IPN_QTY[]': '1',
    'IPN_PRICE[]': '107.00',
    'IPN_VAT[]': '0.00',
    'IPN_VAT_RATE[]': '0.00',
    'IPN_VER[]': '1',
    'IPN_DISCOUNT[]': '0.00',
    'IPN_PROMOTION_CATEGORY[]': '',
    'IPN_PROMONAME[]': '',
    'IPN_PROMOCODE[]': '',
    'IPN_ORDER_COSTS[]': '0',
    'IPN_SKU[]': '',
    'IPN_PARTNER_CODE': '',
    'IPN_PGROUP[]': '0',
    'IPN_PGROUP_NAME[]': '',
    'MESSAGE_ID': '250833683479',
    'MESSAGE_TYPE': 'COMPLETE',
    'IPN_LICENSE_PROD[]': '35144095',
    'IPN_LICENSE_TYPE[]': 'REGULAR',
    'IPN_LICENSE_REF[]': '9WITYHQ6NF',
    'IPN_LICENSE_EXP[]': '2021-04-10 16:29:42',
    'IPN_LICENSE_START[]': '2021-04-08 16:29:42',
    'IPN_LICENSE_LIFETIME[]': 'NO',
    'IPN_LICENSE_ADDITIONAL_INFO[]': '',
    'IPN_DELIVEREDCODES[]': '',
    'IPN_DOWNLOAD_LINK': '',
    'IPN_TOTAL[]': '107.00',
    'IPN_TOTALGENERAL': '107.00',
    'IPN_SHIPPING': '0.00',
    'IPN_SHIPPING_TAX': '0.00',
    'AVANGATE_CUSTOMER_REFERENCE': '884855078',
    'EXTERNAL_CUSTOMER_REFERENCE': '',
    'IPN_PARTNER_MARGIN_PERCENT': '0.00',
    'IPN_PARTNER_MARGIN': '0.00',
    'IPN_EXTRA_MARGIN': '0.00',
    'IPN_EXTRA_DISCOUNT': '0.00',
    'IPN_COUPON_DISCOUNT': '0.00',
    'IPN_LINK_SOURCE': 'testAPI.com',
    'IPN_COMMISSION': '4.1015',
    'REFUND_TYPE': '',
    'IPN_PRODUCT_OPTIONS_35144095_TEXT[]': 'Name LR',
    'IPN_PRODUCT_OPTIONS_35144095_VALUE[]': 'f21a6009c31851ab5166190e353012bd',
    'IPN_PRODUCT_OPTIONS_35144095_OPTIONAL_VALUE[]': 'f21a6009c31851ab5166190e353012bd',
    'IPN_PRODUCT_OPTIONS_35144095_PRICE[]': '7.00',
    'IPN_PRODUCT_OPTIONS_35144095_OPERATOR[]': 'ADD',
    'IPN_PRODUCT_OPTIONS_35144095_USAGE[]': 'PREPAID',
    'CHARGEBACK_RESOLUTION': 'NONE',
    'CHARGEBACK_REASON_CODE': '',
    'TEST_ORDER': '1',
    'IPN_ORDER_ORIGIN': 'API',
    'FRAUD_STATUS': 'APPROVED',
    'CARD_TYPE': 'visa',
    'CARD_LAST_DIGITS': '1111',
    'CARD_EXPIRATION_DATE': '12/22',
    'GATEWAY_RESPONSE': 'Approved',
    'IPN_DATE': '20210408185911',
    'FX_RATE': '1',
    'FX_MARKUP': '0',
    'PAYABLE_AMOUNT': '102.90',
    'PAYOUT_CURRENCY': 'USD',
    'VENDOR_CODE': '250111206876',
    'PROPOSAL_ID': '',
    'HASH': '8d05499f0933c2e07c8599ff3a2e5338'
}


class CplusTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(CplusTestCase, self).setUp()


class CplusSignatureTest(CplusTestCase):
    cplus = None

    def setUp(self):
        super(CplusSignatureTest, self).setUp()
        self.cplus = twocheckout.CplusSignature()

    def test_1_get_signature_without_token_expiration(self):
        self.assertEqual(64, len(self.cplus.get_signature(
            config.TWOCHECKOUT_TEST_MERCHANT_ID,
            config.TWOCHECKOUT_TEST_BUYLINK_SECRET_WORD,
            json_encoded_convert_plus_parameters)))

    def test_1_get_signature_with_token_expiration(self):
        self.assertEqual(64, len(self.cplus.get_signature(
            config.TWOCHECKOUT_TEST_MERCHANT_ID,
            config.TWOCHECKOUT_TEST_BUYLINK_SECRET_WORD,
            json_encoded_convert_plus_parameters,
            1000)))


class ApiTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(ApiTestCase, self).setUp()


class OrderTest(ApiTestCase):
    order = None

    # setup auth headers
    def setUp(self):
        super(OrderTest, self).setUp()
        self.order = twocheckout.Order(auth_params)

    # Get order test
    def test_1_order_get(self):
        self.assertEqual(order_get_test, self.order.get(order_transaction_id))

    # Create order test
    def test_2_order_create(self):
        self.assertEqual('REST_API_AVANGTE', self.order.create(order_params_test)['body']['ExternalReference'])


class IpnHelperTestCase(unittest.TestCase):
    ipn = None

    def setUp(self):
        super(IpnHelperTestCase, self).setUp()
        self.ipn = twocheckout.IpnHelper(config.TWOCHECKOUT_TEST_MERCHANT_SECRET_KEY)

    def test_1_ipn_hash(self):

        self.assertEqual(True, self.ipn.is_valid(ipn_payload))

    def test_2_ipn_calculate_response(self):
        expected = self.calculate_ipn_response(ipn_payload)
        received = self.ipn.calculate_ipn_response(ipn_payload)
        
        self.assertEqual(expected, received)

    def calculate_ipn_response(self, params):
        now = NOW
        result = ''
        ipn_response = {'IPN_PID': [params['IPN_PID[]']],
                        'IPN_NAME': [params['IPN_PNAME[]']],
                        'IPN_DATE': params['IPN_DATE'],
                        'DATE': now.strftime('%Y%m%d%H%M%S')}

        for param in ipn_response:
            if type(ipn_response[param]) is list:
                result += self.expand(ipn_response[param])
            else:
                size = len(ipn_response[param])
                result += str(size) + ipn_response[param]

        return '<EPAYMENT>' + ipn_response['DATE'] + '|' + hmac.new(
            config.TWOCHECKOUT_TEST_MERCHANT_SECRET_KEY.encode(), result.encode(),
            'md5').hexdigest() + '</EPAYMENT>'

    def expand(self, val_list):
        result = ''
        for val in val_list:
            size = len(val.lstrip())
            result += str(size) + str(val.lstrip())
        return result
