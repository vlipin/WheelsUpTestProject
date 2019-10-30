#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from nose.plugins.attrib import attr
import time
import random
from nose.tools import assert_equal
from nose.tools import istest
from tests.base_test import BaseTest


class APIRequestsTest(BaseTest):
    """Class for implementing API tests for Sample project page"""
    # In Tests below any amount of data can be validated.

    def setUp(self):
        super(APIRequestsTest, self).setUp()

    @istest
    @attr(type='API')
    def test_verify_social_accounts(self):
        # Verifying GET data request is OK
        assert_equal(str(self.api_requests.get_request().status_code), "200",
                     "Response code should be 200")
        self._verify_social_accounts("https://twitter.com/WheelsUp", "http://instagram.com/wheelsup8760")

    def _verify_social_accounts(self, twitter, instagram):
        api_data = self.api_requests.get_request().json()
        assert_equal(api_data['keys']['twitter'], twitter, "Twitter link in data json should be {0} "
                                                           ", but found {1}".format(twitter, api_data['keys']['twitter']))

        assert_equal(api_data['keys']['instagram'], instagram, "Instagram link in data json should be {0} "
                                                           ", but found {1}".format(instagram,
                                                                                    api_data['keys']['instagram']))
