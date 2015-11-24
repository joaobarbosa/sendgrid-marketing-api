class CampaignsManager(object):
    u"""Campaings Manager - All campaing methos are available trough this class.

    Args:
        client: instance of SGMarketingClient
    """
    ENDPOINT = '/campaigns'

    def __init__(self, wrapper):
        self.wrapper = wrapper

    def get_all_campaings(self, limit=10, offset=0):
        u"""Get All Campaings

        Args:
            limit: Maximum number of results (SendGrid API default: 10)
            offset: Starting index, where 0 is the first (default: 0)

        Reference: https://sendgrid.com/docs/API_Reference/Web_API_v3/Marketing_Campaigns/campaigns.html#Get-all-Campaigns-GET
        """
        get = {}

        if limit > 0:
            get = {'limit': limit, 'offset': 0}

        return self.wrapper.get(endpoint=CampaignsManager.ENDPOINT, params=get)
