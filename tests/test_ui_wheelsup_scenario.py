#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from nose.plugins.attrib import attr
from nose.tools import istest

from base_test import BaseTest
from page_objects.base_object import BaseObject


class WheelsUpSampleTest(BaseTest):

    def setUp(self):
        super(WheelsUpSampleTest, self).setUp()
        self.base_object = BaseObject()


    @istest
    @attr(type='REGRESSION')
    def test_chat_ui_elements(self):
        """Sample Test scenario ofor Wheels Up pages"""

        self.base_object.go_to_target_page(self.APP_BASE_URL)

        print "Wheels Up start page title is: {0}".format(self.start_page.get_start_page_title_element().text)

        print "Wheels Up contact phone number is: {0}".format(self.start_page.get_phone_number_element().text)

        print "Wheels Up contact Email is: {0}".format(self.start_page.get_email_element().text)

        print "Wheels Up address is: {0}".format(self.start_page.get_address_element().text)

        self.start_page.click_membership_options_menu_element()
        self.start_page.click_core_membership_element()

        print "WheelsUp partial text of 'Becoming a Wheels Up Core Member is easy' is : '{0}'"\
            .format(self.individual_membership.get_become_core_member_section_partial_text())

        self.individual_membership.type_into_first_name_field("Vadym")
        self.individual_membership.type_into_last_name_field("Lipinsky")

        self.individual_membership.click_continue_button()
        self.request_info.type_email_element("vlipinskyy@gmail.com")
        self.request_info.type_phone_element("929-293-5116")
        self.request_info.type_company_name_element("My Test Company")
        self.request_info.type_street_address_element("2001 Hudson Terrace")
        self.request_info.type_city_element("Fort Lee")
        self.request_info.type_zip_element("07024")
        self.request_info.type_state_element("NJ")
        self.request_info.type_country_element("US")
        self.request_info.select_number_of_fligts_over_the_year()
        self.request_info.click_travel_with_pets()
        self.request_info.click_close_button()
