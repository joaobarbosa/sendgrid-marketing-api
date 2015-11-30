from sendgridmarketingapi.wrapper import SendGridClientWrapper
from sendgridmarketingapi.campaigns import CampaignsManager

import pytest
import os


campaign_id = 1


@pytest.fixture
def valid_api_key():
    key = os.getenv('SENDGRID_TEST_API_KEY')

    if not key:
        raise Exception('No API key set in environment.')

    return key


@pytest.fixture
def valid_wrapper():
    return SendGridClientWrapper(valid_api_key())


@pytest.fixture
def valid_campaign_manager():
    return CampaignsManager(valid_wrapper())


@pytest.fixture(scope='session')
def campaign_id_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('cid.txt')
    return fn

# @pytest.fixture
# def set
