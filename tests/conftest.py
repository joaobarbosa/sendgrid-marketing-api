from sendgridmarketingapi.wrapper import SendGridClientWrapper

import pytest
import os


@pytest.fixture
def valid_api_key():
    key = os.getenv('SENDGRID_TEST_API_KEY')

    if not key:
        raise Exception('No API key set in environment.')

    return key


@pytest.fixture
def valid_wrapper():
    apikey = valid_api_key()
    wrapper = SendGridClientWrapper(apikey)

    return wrapper
