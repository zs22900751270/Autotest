#!/usr/bin/env python
# _*_coding:utf-8_*_

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from AppTest.Common.Log import Logger
logger = Logger(logger="AppTest").getlog()


class deviceDriver:
    def __init__(self, driver, sn):
        """
        初始化设备
        """
        self.driver = driver
        self.sn = sn

    def mydriver(self):
        self.DUT = {}
        self.DUT["platformName"] = "Android"
        self.DUT["platformVersion"] = "8.0.0"
        self.DUT["deviceName"] = "KWG5T16A05011645"
        self.DUT["automationName"] = "Uiautomator2"
        self.DUT["noReset"] = "True"
        self.DUT["appPackage"] = "com.huawei.android.launcher"
        self.DUT["appActivity"] = "com.huawei.android.launcher.unihome.UniHomeLauncher"
        try:
            driver = webdriver.Remote("http://localhost:4723/wd/hub", self.DUT)
            time.sleep(4)
            logger.info("获取driver成功")
            return driver
        except WebDriverException:
            logger.info("No driver")

    def myDUT(self):
        """
        返回手机信息
        :return:
        """
        sn = self.DUT['deviceName']
        return sn

