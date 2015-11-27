"""CampaignsManager Test File"""
from sendgridmarketingapi.campaigns import CampaignsManager


class TestCampaigns():
    def test_instantiation(self, valid_wrapper):
        assert CampaignsManager(valid_wrapper)

    def test_get_all_campaigns(self, valid_campaign_manager):
        status, data = valid_campaign_manager.get_all_campaings()

        assert status == 200
