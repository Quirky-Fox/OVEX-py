# OVEX-py
OVEX Python API.

# Installation

    pip install ovex_py


# How to use it

See the tests for detailed usage examples, but basically:

## API object creation

    from ovex_python.client import Client
    c = Client(api_key_id='key_id', base_url='', timeout=0)

Where optional parameters can be passed as follows:

| Parameter   | Description      | Default |
|--------------|------------------|---------|
| api_key_id | Your API key created on the OVEX website | Required for authenticated calls |
| base_url | The API host URL | https://www.ovex.io/api/v2 |
| timeout | The maximum time to wait for requests | 10 (s) |

## API calls

### Get accounts for all currencies

    c.get_accounts()

**Returns**: list of dictionaries containing balances for all currencies

### Get currency info

    c.get_currency_info('btc')

**Returns**: dictionary containing information about the currency requested


### Request a quote

    o.get_quote_rfq(to_amount=1, market='btczar', side='buy')

**Returns**: dictionary containing quote information including a token

# Known Issues

-   Not all error handling has been handled
-   Not all endpoints work as expected, sometimes parameters get ignored
-   Exceptions have not been handled and might not even output a warning

# Acknowledgements

This repo was largely based on the work done on pyluno, thanks to Grant Stephens
https://github.com/grantstephens/pyluno

# To Do

-   Tests for some of the endpoints needing dynamic reponses
-   Add in a rate limiter
-   Add in processing layer to make results more user-friendly


# Contribute

-  Fork it
-  Contribute
-  Test and update