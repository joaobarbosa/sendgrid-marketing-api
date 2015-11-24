from .campaigns import CampaignsManager
from urllib import urlencode

import sendgrid
import json

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
        self.campaigns = CampaignsManager(self)
        self.sg_client = sendgrid.SendGridAPIClient(apikey=apikey, host=SendGridClientWrapper.HOST)

    def _call(self, api_endpoint, method):
        """Execute request in the official client

        Args:
            api_endpoint: instance of API class with endpoint set
            method: method for the request
        """
        if method == SendGridClientWrapper.METHOD_GET:
            return self.sg_client.get(api_endpoint)
        else:
            raise Exception('Undefined request method.')

    def get(self, endpoint, params={}):
        """Execute a GET request

        Args:
            endpoint: string representing a valid API endpoint, like '/campaings'
            params: url parameters as a dict
        """
        if len(params) > 0:
            qs = urlencode(params)
            endpoint = endpoint + '?' + qs

        api_request = API(endpoint)

        status, result = self._call(api_request, SendGridClientWrapper.METHOD_GET)
        json_result = json.loads(result)

        if 'error' in final_result:
            raise Exception(json_result['error'])

        return json_result