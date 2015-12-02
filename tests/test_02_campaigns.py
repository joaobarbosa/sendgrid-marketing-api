"""CampaignsManager Test File"""
from sendgridmarketingapi.campaigns import CampaignsManager
from sendgrid.exceptions import SendGridClientError

import time
import json
import pytest


class TestCampaigns():
    def test_instantiation(self, valid_wrapper):
        assert CampaignsManager(valid_wrapper)

    def test_get_all_campaigns(self, valid_campaign_manager):
        status, data = valid_campaign_manager.get_all_campaigns()

        assert status == 200

    def test_create_campaign(self, valid_campaign_manager, campaign_id_file):
        status, data = valid_campaign_manager.create_campaign(
            'Test campaign - ' + str(int(time.time()))
        )

        assert status == 201

        data_json = json.loads(data)

        campaign_id = data_json['id']

        campaign_id_file.write(str(campaign_id))

        assert campaign_id_file.read() == str(campaign_id)

    def test_get_campaign(self, valid_campaign_manager, campaign_id_file):
        with pytest.raises(SendGridClientError):
            valid_campaign_manager.get_campaign(0)

        campaign_id = int(campaign_id_file.read())

        status, data = valid_campaign_manager.get_campaign(campaign_id)

        assert status == 200

    def test_update_campaign(self, valid_campaign_manager, campaign_id_file):
        with pytest.raises(SendGridClientError):
            valid_campaign_manager.update_campaign(0)

        campaign_id = int(campaign_id_file.read())

        status, data = valid_campaign_manager.update_campaign(
            campaign_id, title='Test campaign upd - ' + str(int(time.time()))
        )

        assert status == 200

    def test_send_campaign(self, valid_campaign_manager, campaign_id_file):
        with pytest.raises(SendGridClientError):
            valid_campaign_manager.send_campaign(0)

        campaign_id = int(campaign_id_file.read())

        with pytest.raises(SendGridClientError):
            valid_campaign_manager.send_campaign(campaign_id)

    def test_delete_campaign(self, request, valid_campaign_manager,
                             campaign_id_file):
        with pytest.raises(SendGridClientError):
            valid_campaign_manager.delete_campaign(0)

        campaign_id = int(campaign_id_file.read())

        status, data = valid_campaign_manager.delete_campaign(campaign_id)

        assert status == 204
