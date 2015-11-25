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
    (METHOD_GET, METHOD_POST) = (1, 2)

    def __init__(self, apikey):
        self.sg_client = sendgrid.SendGridAPIClient(
            apikey=apikey,
            host=SendGridClientWrapper.HOST
        )

    def _call(self, api_endpoint, method):
        """Execute request in the official client

        Args:
            api_endpoint: instance of API class with endpoint set
            method: method for the request
        """
        if method == SendGridClientWrapper.METHOD_GET:
            return self.sg_client.get(api_endpoint)

        raise UnknownRequestMethodException('Unknown request method.')

    def get(self, endpoint, **params):
        """Execute a GET request

        Args:
            endpoint: string representing a valid API endpoint,
                      like '/campaings'
            params: url parameters as a dict
        """
        if params:
            qs = urlencode(params)
            endpoint = endpoint + '?' + qs

        return self._call(
            API(endpoint),
            SendGridClientWrapper.METHOD_GET
        )
