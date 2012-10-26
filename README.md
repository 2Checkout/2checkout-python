2Checkout Python Library
=====================

This library provides developers with a simple set of bindings to the 2Checkout purchase routine, Instant Notification Service and Back Office API.

To use, download or clone the repository.

```shell
git clone https://github.com/craigchristenson/2checkout-python.git
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

Full documentation for each binding will be provided in the [Wiki](https://github.com/craigchristenson/2checkout-python/wiki).


Example API Usage
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
