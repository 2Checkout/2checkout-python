
from distutils.core import setup
setup(
    name="twocheckout",
    version='2.0.0',
    description="2Checkout Python Library using API 6.0",
    author="2Checkout",
    author_email="supportplus@2checkout.com",
    url="https://www.2checkout.com",
    packages=["twocheckout"],
    python_requires=">=3.5",
    install_requires=[
        'requests >= 2.20; python_version >= "3.5"; pyjwt >= 19.2'
    ]
)
