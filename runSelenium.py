#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import time
import unittest

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BROWSERSTACK_ACCESSKEY = "cW4x2PdANhexdBwPLWxC"
BROWSERSTACK_USERNAME = "nozomumiura1"
BROWSERSTACK_ENDPOINT = 'http://{}:{}@hub.browserstack.com:80/'.format(
    BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESSKEY)

#class SampleTest1(unittest.TestCase):
#    def setUp(self):
#        desired_cap = {
#            'os' : 'Windows',
#            'os_version' : '10',
#            'browser' : 'Chrome',
#            'browser_version' : '68.0',
#            'project': project,
#            'name': self.__class__.__name__,
#            'build': gitHash,
#            'browserstack.local': 'false',
#            'browserstack.debug': 'true',
#            'browserstack.selenium_version': '3.5.2'
#        }
#        self.driver = webdriver.Remote(
#            command_executor=BROWSERSTACK_ENDPOINT + '/wd/hub',
#            desired_capabilities=desired_cap)
#
#    def test_sample(self):
#        #try:
#            self.driver.get("https://front----.herokuapp.com/")
#            wait = WebDriverWait(self.driver, 10)
#            wait.until(EC.presence_of_all_elements_located)
#            time.sleep(5)
#            elems = self.driver.find_elements(By.ID, 'now')
#            for actual in elems:
#                self.assertTrue('GMT' in actual.text)
#        # except AssertionError as e:
#        #    requests.put(
#        #        BROWSERSTACK_ENDPOINT + '/automate/sessions/{}.json'.format(
#        #            self.driver.session_id),
#        #        data={
#        #            "status": "fail",
#        #            "reason": str(e)
#        #        })
#        #    raise e
#
#    def tearDown(self):
#        self.driver.quit()


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        url = 'http://nozomumiura1:cW4x2PdANhexdBwPLWxC@hub.browserstack.com:80/wd/hub'
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=DesiredCapabilities.FIREFOX)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.submit()
        self.assertIn("Google", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    gitHash = sys.argv[1]
    project = sys.argv[2]
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(verbosity=3).run(suite)
