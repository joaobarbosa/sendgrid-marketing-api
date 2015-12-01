class CampaignsManager(object):
    """Campaigns Manager - All campaign methos are available trough this class.

    All methods here can raise SendGrid exceptions:
        SendGridClientError, SendGridServerError

    Args:
        client: instance of SGMarketingClient
    """
    ENDPOINT = '/campaigns'

    def __init__(self, wrapper):
        self.wrapper = wrapper

    def get_all_campaigns(self, limit=10, offset=0):
        """Get All Campaigns

        Can raise SendGrid exceptions: SendGridClientError, SendGridServerError

        Args:
            limit: (int) Maximum number of results (SendGrid API default: 10)
            offset: (int) Starting index, where 0 is the first (default: 0)

        Reference: https://sendgrid.com/docs/API_Reference/Web_API_v3
                   /Marketing_Campaigns/campaigns.html#Get-all-Campaigns-GET
        """
        get = {}

        if limit > 0:
            get = {'limit': limit, 'offset': 0}

        return self.wrapper.get(endpoint=CampaignsManager.ENDPOINT, **get)

    def create_campaign(self, title, **params):
        """Create Campaign

        Args:
            title: (str) Campaign title (max. of 100 characters)

            **params:
                subject: (str) (optional) Email subject
                sender_id: (int) (optional) Sender ID
                list_ids: (dict) (optional) List IDs
                segment_ids: (dict) (optional) Segment IDs
                categories: (dict) (optional) List of categories
                suppression_group_id: (int) (optional) Suppression Group ID
                custom_unsubscribe_url: (str) (optional) Custom unsubscribe URL
                ip_pool: (str) (optional) IP pool
                html_content: (str) (optional) Email content in HTML
                plain_content: (str) (optional) Email content in plain text

        Reference: https://sendgrid.com/docs/API_Reference/Web_API_v3
                   /Marketing_Campaigns/campaigns.html#Create-a-Campaign-POST
        """
        params['title'] = title

        return self.wrapper.post(endpoint=CampaignsManager.ENDPOINT, **params)

    def get_campaign(self, campaign_id):
        return self.wrapper.get(
            endpoint=CampaignsManager.ENDPOINT + '/' + str(campaign_id)
        )

    def delete_campaign(self, campaign_id):
        return self.wrapper.delete(
            endpoint=CampaignsManager.ENDPOINT + '/' + str(campaign_id)
        )
