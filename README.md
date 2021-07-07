2Checkout Python Library
=====================

This library provides developers with a simple set of bindings to the 2Checkout API, Checkout and IPN.

To use, download or clone the repository.

```shell

git clone https://github.com/2checkout/2checkout-python.git

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


*Example Usage:*

You can browse through the /examples folder to see how new order is placed, get an order from 2CO API side, create a
subscription, etc

IPN must be validated before you deal with the request. We create a helper class for you to ease you process intro
validate the request. After you add your IPN url intro 2Checkout account (IPN Settings area), your will receive updates
from our API. Instantiate the IpnHelper class with your secret key, validate the request using the `is_valid` function,
then you can update your order, subscription etc. After you validate the request and do your thing, you must use
the `calculate_ipn_response` to response the 2Checkout API with our custom response <EPAYMENT>date|hash</EPAYMENT>
