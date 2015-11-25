"""SendGridClientWrapper Test File"""

from sendgridmarketingapi.wrapper import SendGridClientWrapper, API
from sendgridmarketingapi.exceptions import UnknownRequestMethodException
from sendgrid.exceptions import SendGridClientError

import json
import pytest

VALID_ENDPOINT = '/campaigns'
VALID_GET_PARAMS = {'limit': 100, 'offset': 0}


class TestWrapper():
    def test_instantiation_api(self):
        with pytest.raises(TypeError):
            API()

        api = API('/endpoint')

        assert api.endpoint is '/endpoint'

    def test_instantiation_and_get(self, valid_api_key):
        with pytest.raises(TypeError):
            SendGridClientWrapper()

        with pytest.raises(SendGridClientError):
            wrapper = SendGridClientWrapper('wrong-key')
            status, data = wrapper.get(endpoint=VALID_ENDPOINT)
            response_json = json.loads(data)

            assert status == 401
            assert 'errors' in response_json

        wrapper = SendGridClientWrapper(valid_api_key)
        status, data = wrapper.get(endpoint=VALID_ENDPOINT)

        assert status == 200

        status, data = wrapper.get(
            endpoint=VALID_ENDPOINT,
            params=VALID_GET_PARAMS
        )

        assert status == 200

    def test_call_unknown_request(self, valid_api_key):
        wrapper = SendGridClientWrapper(valid_api_key)

        with pytest.raises(UnknownRequestMethodException):
            wrapper._call(api_endpoint=VALID_ENDPOINT, method=99)
