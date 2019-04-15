#!/usr/bin/env python
# _*_coding:utf-8_*_

import HTMLTestRunner, warnings, shutil, threading
import unittest, configparser, time, logging
import datetime, os, pymysql, redis, re

config = configparser.ConfigParser()
try:
    config.read("config.ini")
    project_path = config.get("projectPath", "project_path")
    browser = config.get("browserType", "browserName")
except:
    grader_father = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "..")
    config.read(grader_father + "/config.ini")
    project_path = config.get("projectPath", "project_path")
    browser = config.get("browserType", "browserName")

report_path = project_path + "/report"
LogPath = project_path + "/Logs/"


class AllTest:
    def __init__(self):
        # 创建report文件夹
        if not os.path.exists(report_path): os.mkdir(report_path)

        # 在report文件夹中创建截图文件夹
        self.srceen_shot_path = self.get_screen_shot_path()
        print(self.srceen_shot_path)
        os.mkdir(self.srceen_shot_path)
        self.caseFile = project_path + "/testCase"

    def get_screen_shot_path(self):
        """设置截图文件夹"""
        now_t = datetime.datetime.strftime(datetime.datetime.now(), "%Y_%m_%d_%H_%M_%S")
        pic_con = configparser.ConfigParser()
        pic_con.read("config.ini")
        pic_con.set("screenShot", "screenshot_folder_name", report_path + "/All_case_list/screen_shot_%s" % now_t)
        if not os.path.exists(report_path + "/All_case_list"): os.mkdir(report_path + "/All_case_list")
        with open("config.ini", "w+") as f:
            pic_con.write(f)
        return report_path + "/All_case_list/screen_shot_%s" % now_t

    def set_case_list(self, caselist_path):
        """
        set case list
        :return:
        """
        fb = open(caselist_path)
        for value in fb.readlines():
            data = str(value)
            if data is not None and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self, caselist_path):
        """
        set case suite
        :return:
        """
        self.set_case_list(caselist_path)
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name)
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name, top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self, caselist_path):
        """
        run test
        :return:
        """
        self.caseList = []
        print("*********TEST START*********")
        try:
            testsuit = self.set_case_suite(caselist_path)
            if testsuit is not None:
                now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                filename = report_path + "/All_case_list/" + now + "_result.html"
                fp = open(filename, "wb")
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试报告", description="测试报告如下所示",
                tester="zhangsen", screen_shot_path=self.srceen_shot_path)
                runner.run(testsuit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
        finally:
            print("*********TEST END*********")
            fp.close()


if __name__ == '__main__':
    t = AllTest()
    # t.run(project_path + "/caselist_android.txt")
    # t.run(project_path + "/caselist_client.txt")
    t.run(project_path + "/caselist_portal.txt")
    # t.run(project_path + "/caselist.txt")
