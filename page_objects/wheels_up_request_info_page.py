#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from base_object import BaseObject


class WheelsUpRequestInfoPage(BaseObject):
    """@description: class with element getters and action methods for Wheels Up request info page
           @author: vlipinskyy"""

    def __init__(self):
        super(WheelsUpRequestInfoPage, self).__init__()
        self.wait = WebDriverWait(self.driver, self._test_timeout)

    def get_email_element(self):
        return self.get_element_by_css("input#Email-clone")

    def get_phone_number_element(self):
        self.actions.move_to_element(self.get_element_by_css("input#Phone-clone")).perform()
        return self.get_element_by_css("input#Phone-clone")

    def get_company_name_element(self):
        self.actions.move_to_element(self.get_element_by_css("input#Company__c-clone")).perform()
        return self.get_element_by_css("input#Company__c-clone")

    def get_street_address_element(self):
        self.actions.move_to_element(self.get_element_by_css("input#Address-clone")).perform()
        return self.get_element_by_css("input#Address-clone")

    def get_city_element(self):
        return self.get_element_by_css("input#City-clone")

    def get_zip_element(self):
        return self.get_element_by_css("input#PostalCode-clone")

    def get_state_element(self):
        return self.get_element_by_css("input#State-clone")

    def get_country_element(self):
        return self.get_element_by_css("input#Country-clone")

    def type_email_element(self, text):
        self.get_email_element().send_keys(text)

    def type_phone_element(self, text):
        self.get_phone_number_element().send_keys(text)

    def type_company_name_element(self, text):
        self.get_company_name_element().send_keys(text)

    def type_street_address_element(self, text):
        self.get_street_address_element().send_keys(text)
        self.actions.send_keys(Keys.TAB).perform()

    def type_city_element(self, text):
        self.get_city_element().send_keys(text)

    def type_zip_element(self, text):
        self.get_zip_element().send_keys(text)

    def type_state_element(self, text):
        self.get_state_element().send_keys(text)

    def type_country_element(self, text):
        self.get_country_element().send_keys(text)

    def select_number_of_fligts_over_the_year(self):
        option_num = random.randrange(0, 3)
        self.actions.move_to_element(
            self.get_element_by_css("input[name='Do_you_have_a_need_to_travel_with_pets__c']")).perform()
        self.get_element_by_css("div#How_Many_Private_Flights_Per_Year__c-clone0 span").click()
        self.actions.move_to_element(
            self.get_element_by_css("div#Do_you_own_or_travel_to_a_second_home__c-cloneYes")).perform()
        option_elements = self.get_elements_by_css("div.dropdown-box.active>ul>li")
        option_elements[option_num].click()

    def click_travel_with_pets(self):
        self.actions.move_to_element(
            self.get_element_by_css("div#Do_you_own_or_travel_to_a_second_home__c-cloneYes")).perform()
        self.get_element_by_css("label[for='mktoRadio_78443_0-clonecss']").click()

    def select_do_you_own_or_element(self):
        option_num = random.randrange(0, 1)
        self.actions.move_to_element(
            self.get_element_by_css("div#How_does_the_Lead_currently_Travel__c-clone")).perform()
        self.get_element_by_css("div#Do_you_own_or_travel_to_a_second_home__c-cloneYes span").click()
        option_elements = self.get_elements_by_css("div.dropdown-box.active>ul>li")
        option_elements[option_num].click()

    def click_close_button(self):
        self.get_element_by_css("div>i.icon-close").click()

