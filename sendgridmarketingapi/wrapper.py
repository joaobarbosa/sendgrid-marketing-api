from .exceptions import UnknownRequestMethodException
from urllib import urlencode

import sendgrid


class API(object):
    """Workaround for using SendGrid official API client.

    Args:
        endpoint: string representing a valid API endpoint, like '/campaings'
    """
    def __init__(self, endpoint):
        self.endpoint = endpoint


class SendGridClientWrapper(object):
    """SendGridClientWrapper - Custom client, relies on the official client

    Args:
        api_key: Your SendGrid API key
    """
    HOST = 'https://api.sendgrid.com/v3'
    (METHOD_GET, METHOD_POST, METHOD_PATCH, METHOD_DELETE) = (1, 2, 3, 4)

    def __init__(self, apikey):
        self.sg_client = sendgrid.SendGridAPIClient(
            apikey=apikey,
            host=SendGridClientWrapper.HOST
        )

    def _call(self, api_endpoint, method, data=None):
        """Execute request in the official client

        Args:
            api_endpoint: (API) instance of API class with endpoint set
            method: (int) method for the request
        """
        if method == SendGridClientWrapper.METHOD_GET:
            return self.sg_client.get(api_endpoint)

        if method == SendGridClientWrapper.METHOD_POST:
            return self.sg_client.post(api_endpoint, data)

        if method == SendGridClientWrapper.METHOD_DELETE:
            return self.sg_client.delete(api_endpoint)

        raise UnknownRequestMethodException('Unknown request method.')

    def get(self, endpoint, **params):
        """Execute a GET request

        Args:
            endpoint: (str) valid API endpoint, like '/campaings'
            params: (dict) url parameters
        """
        if params:
            qs = urlencode(params)
            endpoint = endpoint + '?' + qs

        return self._call(API(endpoint), SendGridClientWrapper.METHOD_GET)

    def post(self, endpoint, **params):
        """Execute a POST request

        Args:
            endpoint: (str) valid API endpoint, like '/campaings'
            params: (dict) post data
        """
        return self._call(
            API(endpoint),
            SendGridClientWrapper.METHOD_POST,
            params
        )

    def delete(self, endpoint):
        """Execute a DELETE request

        Args:
            endpoint: (str) valid API endpoint, like '/campaings/{id}'
        """
        return self._call(
            API(endpoint),
            SendGridClientWrapper.METHOD_DELETE
        )
