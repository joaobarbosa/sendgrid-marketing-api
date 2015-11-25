"""CampaignsManager Test File"""
from sendgridmarketingapi.campaigns import CampaignsManager


class TestCampaigns():
    def test_instantiation(self, valid_wrapper):
        assert CampaignsManager(valid_wrapper)

    def test_get_all_campagins(self, valid_wrapper):
        manager = CampaignsManager(valid_wrapper)

        status, data = manager.get_all_campaings()

        assert status == 200
