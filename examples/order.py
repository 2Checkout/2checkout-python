import twocheckout

# fill you MERCHANT_CODE & SECRET_KEY from 2Checkout account page
auth_params = {
    'merchant_code': '250111206876',
    'secret_key': '=B6gcTl(4t8@D3yUM!TP'
}

# Transaction ID example
order_transaction_id = '147288494'

# order params ( when creating new orders use this JSON format (some fields are optional)
# to view what are the required or optional fields please read the our docs
order_params = {
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
# # instantiate the object ( for auth)
order = twocheckout.order.Order(auth_params)

## creates a new order
new_order = order.create(order_params)

## get full info for an order
get_order = order.get(order_transaction_id)

print('new order')
print(new_order)
print('#########################')
print('get order ')
print(get_order)
