#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest

from code_base.http_requests import SampleHTTPRequests
from code_base.webdriver_factory import WebdriverFactory
from page_objects.wheels_up_start_page import WheelsUpStartPage
from page_objects.wheels_up_individual_membership_page import WheelsUpIndividualMembershipPage
from page_objects.wheels_up_request_info_page import WheelsUpRequestInfoPage


class BaseTest(unittest.TestCase):
    """@description: class to provide SetUp and TearDown as well as global vars
               @author: vlipinskyy"""

    APP_BASE_URL = "https://wheelsup.com"

    def setUp(self):
        self.start_page = WheelsUpStartPage()
        self.individual_membership = WheelsUpIndividualMembershipPage()
        self.request_info = WheelsUpRequestInfoPage()
        self.api_requests = SampleHTTPRequests()

    def tearDown(self):
        try:
            WebdriverFactory().quit_driver()
        except Exception.message as e:
            print "Issue has appeared with quitting WebDriver.. Please, re-run test suite: ".format(e)

    if __name__ == '__main__':
        unittest.main(verbosity=2)