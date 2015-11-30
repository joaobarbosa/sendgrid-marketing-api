# SendGrid Marketing API Wrapper

[![Requirements Status](https://requires.io/github/joaobarbosa/sendgrid-marketing-api/requirements.svg?branch=master)](https://requires.io/github/joaobarbosa/sendgrid-marketing-api/requirements/?branch=master)

**Unnoficial** wrapper for interacting with the [SendGrid's Web API V3](https://sendgrid.com/docs/API_Reference/Web_API_v3/).

Supports Python 2.7+. **NOT TESTED IN PYTHON 3** (yet).

## Requirements

Check the ```requirements.txt``` for a complete list of dependecies of this library.

Install everything it needs with ```pip install -r /path/to/requirements.txt```

## Basic usage

```python
from sendgridmarketingapi.wrapper import SendGridClientWrapper
from sendgridmarketingapi.campaigns import CampaignsManager

apikey = 'your-sendgrid-api-key'
client = SendGridClientWrapper(apikey)
campaign_manager = CampaignsManager(client)

status, data = campaign_manager.get_all_campaigns()
```

## Testing

Tests were built using [Py.test](https://pytest.org/) with some extensions (pytest-cov, pytest-pep8) and [Radon](https://pypi.python.org/pypi/radon).

Check the ```requirements.txt``` for a complete list of dependecies of this library.

### Running tests

**Note**: You should set up an environment variable named **SENDGRID_TEST_API_KEY** with an valid api key for testing. If you didn't set it before, the script will ask before running the tests.

```sh
cd /path/to/tests

./runtests.sh
```
