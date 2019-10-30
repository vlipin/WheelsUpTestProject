#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from base_object import BaseObject


class WheelsUpIndividualMembershipPage(BaseObject):
    """@description: class with element getters and action methods for Wheels Up individual page
           @author: vlipinskyy"""

    def __init__(self):
        super(WheelsUpIndividualMembershipPage, self).__init__()
        self.wait = WebDriverWait(self.driver, self._test_timeout)

    def get_become_core_member_section_partial_text(self):
        self.wait_given_time(4)
        return self.get_element_by_xpath("//*[text()='Becoming a Wheels Up Core Member is easy']/following-sibling::p").text[24:47]

    def get_first_name_field_element(self):
        self.actions.move_to_element(self.get_element_by_xpath("//*[text()='Learn More']")).perform()
        return self.get_element_by_css("input#FirstName-clone")

    def get_last_name_field_element(self):
        self.actions.move_to_element(self.get_element_by_xpath("//*[text()='Learn More']")).perform()
        return self.get_element_by_css("input#LastName-clone")

    def get_continue_button(self):
        self.actions.move_to_element(self.get_element_by_xpath("//*[text()='Learn More']")).perform()
        return self.get_element_by_xpath("//*[text()=' CONTINUE ']")

    def click_continue_button(self):
        self.get_continue_button().click()
        self.wait_given_time(2)

    def type_into_first_name_field(self, text):
        self.get_first_name_field_element().send_keys(text)

    def type_into_last_name_field(self, text):
        self.get_last_name_field_element().send_keys(text)
