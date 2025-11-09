"""
Payment Processor README
=========================

Overview
--------

This is a Python-based payment processing system designed for simplicity and scalability.

Requirements
------------

* Python 3.8+
* requests library for API interactions
* PyJWT library for token management

Installation
------------

To install the required libraries, run the following command:

```bash
pip install requests pyjwt
```

Configuration
------------

To configure the payment processor, create a `config.json` file with the following structure:

```json
{
    "payment_gateway": "https://your-payment-gateway.com",
    "api_key": "your-api-key",
    "api_secret": "your-api-secret"
}
```

Usage
-----

To use the payment processor, import the module and initialize it with the `config.json` file:

```python
import payment_processor

config = payment_processor.load_config("config.json")
processor = payment_processor.PaymentProcessor(config)
```

You can then use the `processor` object to process payments:

```python
processor.charge_card(card_number, expiration_date, cvv)
```

API Documentation
-----------------

### PaymentProcessor

#### Methods

* `charge_card(card_number, expiration_date, cvv)`:
    + Charges the specified card with the given details.
    + Returns a payment token if successful.

#### Attributes

* `config`: The configuration object loaded from the `config.json` file.
* `gateway`: The payment gateway URL.
* `api_key`: The API key for the payment gateway.
* `api_secret`: The API secret for the payment gateway.

#### Exceptions

* `PaymentError`: Raised when a payment error occurs.
* `ConfigError`: Raised when a configuration error occurs.