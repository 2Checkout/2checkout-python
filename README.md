2Checkout Python Library
=====================

This library provides developers with a simple set of bindings to the 2Checkout purchase routine, Instant Notification Service and Back Office API.

To use, download or clone the repository.

```shell
git clone https://github.com/2checkout/2checkout-python.git
```

If your using python version 3.0 or higher, checkout the 3.x branch.

```shell
git checkout 3.x
```

Install _(Or just import in your script.)_

```shell
cd 2checkout-python
sudo python setup.py install
```

Import in your script

```python
import twocheckout
```

Full documentation for each binding will be provided in the [Wiki](https://github.com/2checkout/2checkout-python/wiki).

Example Purchase API Usage
-----------------

*Example Usage:*

```python
import twocheckout


twocheckout.Api.auth_credentials({
    'private_key': '3508079E-5383-44D4-BF69-DC619C0D9811',
    'seller_id': '1817037',
    'mode': 'production'
})

params = {
    'merchantOrderId': '123',
    'token': 'ODAxZjUzMDEtOWU0MC00NzA3LWFmMDctYmY1NTQ3MDhmZDFh',
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

try:
    result = twocheckout.Charge.authorize(params)
    print result.responseCode
except twocheckout.TwocheckoutError as error:
    print error.msg

```

*Example Response:*

```python
{
    'lineItems': [
        {
            'tangible': 'N',
            'name': '123',
            'price': '1.00',
            'description': '',
            'recurrence': None,
            'duration': None,
            'startupFee': None,
            'productId': '',
            'type': 'product',
            'options': [
                
            ],
            'quantity': '1'
        }
    ],
    'responseMsg': 'Successfully authorized the provided creditcard',
    'recurrentInstallmentId': None,
    'shippingAddr': {
        'city': None,
        'phoneExtension': None,
        'country': None,
        'addrLine2': None,
        'zipCode': None,
        'addrLine1': None,
        'state': None,
        'phoneNumber': None,
        'email': None,
        'name': None
    },
    'orderNumber': '205180784763',
    'currencyCode': 'USD',
    'merchantOrderId': '123',
    'errors': None,
    'responseCode': 'APPROVED',
    'transactionId': '205180784772',
    'total': '1.00',
    'type': 'AuthResponse',
    'billingAddr': {
        'city': 'Columbus',
        'phoneExtension': None,
        'country': 'USA',
        'addrLine2': None,
        'zipCode': '43123',
        'addrLine1': '123 Test St',
        'state': 'OH',
        'phoneNumber': '555-555-5555',
        'email': 'cchristenson@2co.com',
        'name': 'Testing Tester'
    }
}
```

Example Admin API Usage
-----------------

*Example Usage:*

```python
import twocheckout


twocheckout.Api.credentials({'username':'APIuser1817037', 'password':'APIpass1817037'})

params = {
    'sale_id': 4774467596,
    'category': 1,
    'comment': "Refunding Sale"
    }

sale = twocheckout.Sale.find(params)
sale.refund(params);
```

*Example Response:*

```python
{
  'response_code': 'OK', 
  'response_message': 'refund added to invoice'
}
```

Example Checkout Usage:
-----------------------

*Example Usage:*

```python
params = {
    'sid': 1817037,
    'cart_order_id': 'test1',
    'total': 1.00
}

form = twocheckout.Charge.submit(params)
```
*Example Response:*

```html
<form id='2checkout' action='https://www.2checkout.com/checkout/spurchase' method='post'>
<input type='hidden' name='li_0_name' value='Test Product' />
<input type='hidden' name='li_0_price' value='0.01' />
<input type='hidden' name='mode' value='2CO' />
<input type='hidden' name='sid' value='1817037' />
<input type='submit' value='Proceed to Checkout' />
</form>
<script type='text/javascript'>document.getElementById('2checkout').submit();</script>
```

Example Return Usage:
---------------------

*Example Usage:*

```python
params = web.input() # using web.py
params['secret'] = 'tango'
result = twocheckout.Passback.check(params)
```

*Example Response:*

```python
{
  'response_code': 'SUCCESS', 
  'response_message': 'Hash Matched'
}
```

Example INS Usage:
------------------

*Example Usage:*

```python
params = web.input() # using web.py
params['secret'] = 'tango'
result = twocheckout.Notification.check(params)
```

*Example Response:*

```python
{
  'response_code': 'SUCCESS', 
  'response_message': 'Hash Matched'
}
```

Full documentation for each binding is provided in the [Wiki](https://github.com/craigchristenson/2checkout-python/wiki).

Exceptions:
-----------
TwocheckoutError exceptions are thrown by if an error has returned. It is best to catch these exceptions so that they can be gracefully handled in your application.

*Example Usage*

```python
try:
    sale = twocheckout.Sale.find(EXAMPLE_SALE)
    invoice = sale.invoices[0]
    lineitem = invoice.lineitems[0]
    result = lineitem.refund(EXAMPLE_REFUND)
except TwocheckoutError as error:
    error.message
```
