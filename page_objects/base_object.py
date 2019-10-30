#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import NoSuchElementException, WebDriverWait
from code_base.webdriver_factory import WebdriverFactory
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BaseObject(object):
    """@description: class with overwritten WebDriver functions and additional features to handle page elements
       @author: vlipinskyy"""

    BROWSER_DESKTOP = "mac_chrome"
    BROWSER_MOBILE = "mac_chrome_mobile"

    def __init__(self):
        self.driver = WebdriverFactory().get_driver(self.BROWSER_DESKTOP)
        self.actions = ActionChains(self.driver)
        self._test_timeout = 10

    def get_element_by_class(self, elem_class, timeout=10):
        """Function to wait until element is located on the page and then return it using CSS
           :param
                    css - unique css selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.CLASS_NAME, elem_class)))
        except NoSuchElementException.message as e:
            # Exception of No needed element is found
            print "Element is not found by CLASS on the page after timeout of" + str(timeout) + e

        return self.driver.find_element_by_class_name(elem_class)

    def get_element_by_id(self, id, timeout=10):
        """Function to wait until element is located on the page and then return it using ID
           :param
                    id - unique id selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            self.actions.move_to_element(self.driver.find_element_by_id(id)).perform()
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.ID, id)))
        except NoSuchElementException.message as e:
            # Exception of No needed element is found
            print "Element is not found by ID on the page after timeout of" + str(timeout) + e

        return self.driver.find_element_by_id(id)

    def get_element_by_css(self, css, timeout=10):
        """Function to wait until element is located on the page and then return it using CSS
           :param
                    css - unique css selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            self.actions.move_to_element(self.driver.find_element_by_css_selector(css)).perform()
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except NoSuchElementException.message as e:
            # Exception of No needed element is found
            print "Element is not found by CSS on the page after timeout of" + str(timeout) + e

        return self.driver.find_element_by_css_selector(css)

    def get_element_by_xpath(self, xpath, timeout=10):
        """Function to wait until element is located on the page and then return it using XPATH
           :param
                    xpath - unique xpath selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over
           :return WebElement
        """
        try:
            self.actions.move_to_element(self.driver.find_element_by_xpath(xpath)).perform()
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except NoSuchElementException.message as e:
            # Exception of No needed element is found
            print "Element is not found by XPATH on the page after timeout of" + str(timeout) + e

        return self.driver.find_element_by_xpath(xpath)

    def get_elements_by_css(self, css, timeout=2000):
        """Function to wait until element group is located on the page and then return it using CSS
           :param
                    css - unique css selector for group of elements
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except NoSuchElementException.message as e:
            # Exception of No needed element is found
            print "Any Element of Elements was not found by CSS on the page after timeout of" + str(timeout) + e

        return self.driver.find_elements_by_css_selector(css)

    def go_to_target_page(self, url):
        """Function to get the target page by URL
           :param url - exact url of the page
        """
        self.driver.get(url)

    def wait_given_time(self, timeout):
        """Function to wait forcefully given amount of time in seconds, for post time test"""
        time.sleep(timeout)
