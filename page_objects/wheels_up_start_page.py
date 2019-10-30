#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from base_object import BaseObject


class WheelsUpStartPage(BaseObject):
    """@description: class with element getters and action methods for Wheels Up start page
           @author: vlipinskyy"""

    def __init__(self):
        super(WheelsUpStartPage, self).__init__()
        self.wait = WebDriverWait(self.driver, self._test_timeout)

    def get_start_page_title_element(self):
        self.wait_given_time(4)
        return self.get_element_by_css("h1.heading.ui-reveal")

    def get_phone_number_element(self):
        self.actions.move_to_element(self.get_element_by_css("span.link.white.text.ng-star-inserted")).perform()
        return self.get_element_by_css("span.link.white.text.ng-star-inserted")

    def get_email_element(self):
        self.actions.move_to_element(self.get_element_by_css("a[href='mailto:info@wheelsup.com']")).perform()
        return self.get_element_by_css("a[href='mailto:info@wheelsup.com']")

    def get_address_element(self):
        self.actions.move_to_element(self.get_element_by_css("span.base-label")).perform()
        return self.get_element_by_css("span.base-label")

    def get_membership_options_menu_element(self):
        return self.get_element_by_xpath("//*[text()=' Membership Options ']")

    def get_core_membership_element(self):
        if (len(self.get_elements_by_css("div.menu-item>ul")) is 0):
            self.get_membership_options_menu_element().click()
            return self.get_element_by_css("ul.menu-item-container>li:nth-child(2)>a")
        else:
            return self.get_element_by_css("ul.menu-item-container>li:nth-child(2)>a")

    def click_membership_options_menu_element(self):
        self.get_membership_options_menu_element().click()

    def click_core_membership_element(self):
        self.get_core_membership_element().click()

