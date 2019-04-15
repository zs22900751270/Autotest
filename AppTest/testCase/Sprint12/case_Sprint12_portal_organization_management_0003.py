#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""pc—创建部门，部门名称长度限制"""
        logger.info("登录后端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "新建部门", "button")

        logger.info("查看部门名称与主管长度是否有长度限制")
        ele_1 = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入部门名称")
        ele_2 = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入部门主管手机号码")
        self.assertEqual(ele_1.get_attribute("maxlength"), "50")
        self.assertEqual(ele_2.get_attribute("maxlength"), "11")


