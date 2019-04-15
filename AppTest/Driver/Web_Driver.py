#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.TestRunner import *
from selenium import webdriver
from AppTest.Common.Log import Logger
logger = Logger(logger="WebTest").getlog()


class BrowserEngine(object):
    def __init__(self, web_driver):
        self.driver = web_driver
        # read the browser type from config.ini file, return the driver

    def open_browser(self, web_driver, url):
        logger.info("You had select %s browser." % browser)
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            web_driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            web_driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "Edge":
            web_driver = webdriver.Edge()
            logger.info("Starting Edge browser.")

        web_driver.get(url)
        logger.info("Open url: %s" % url)
        web_driver.maximize_window()
        logger.info("Maximize the current window.")
        web_driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return web_driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.web_driver.quit()
