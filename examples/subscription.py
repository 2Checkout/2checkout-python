import twocheckout

# fill you VENDOR_ID & SECRET_KEY from 2Checkout account page
auth_params = {
    'merchant_code': '250111206876',
    'secret_key': '=B6gcTl(4t8@D3yUM!TP'
}

# Transaction ID example
subscription_id = '37A4678B13'

subscription_params = {
    "CustomPriceBillingCyclesLeft": 2,
    "DeliveryInfo": {
        "Codes": [
            {
                "Code": "___TEST___CODE____"
            }
        ]
    },
    "EndUser": {
        "Address1": "Test Address",
        "Address2": "",
        "City": "LA",
        "Company": "",
        "CountryCode": "us",
        "Email": "customer@2Checkout.com",
        "Fax": "",
        "FirstName": "Customer",
        "Language": "en",
        "LastName": "2Checkout",
        "Phone": "",
        "State": "CA",
        "Zip": "12345"
    },
    "ExpirationDate": "2015-12-16",
    "ExternalSubscriptionReference": "ThisIsYourUniqueIdentifier123",
    "NextRenewalPrice": 49.99,
    "NextRenewalPriceCurrency": "usd",
    "PartnerCode": "",
    "Payment": {
        "CCID": "123",
        "CardNumber": "4111111111111111",
        "CardType": "VISA",
        "ExpirationMonth": "12",
        "ExpirationYear": "2018",
        "HolderName": "John Doe"
    },
    "Product": {
        "PriceOptionCodes": [
            "addon-1_1_annually"
        ],
        "ProductCode": "my_subscription_1",
        "ProductId": "24584760",
        "ProductName": "2Checkout Subscription",
        "ProductQuantity": 1,
        "ProductVersion": ""
    },
    "StartDate": "2015-02-16",
    "SubscriptionValue": 199,
    "SubscriptionValueCurrency": "usd",
    "Test": 1
}

# instantiate the object ( for auth)
subscription = twocheckout.subscription.Subscription(auth_params)

# creates a new subscription
new_subscription = subscription.create(subscription_params)

# get full info for an subscription
get_subscription = subscription.get(subscription_id)

print('new subscription')
print(new_subscription)
print('#########################')
print('get subscription ')
print(get_subscription)
