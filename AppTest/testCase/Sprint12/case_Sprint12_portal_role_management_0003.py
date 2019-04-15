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
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.quit(self)

    def test_step(self):
        u"""管理端-角色管理-新建角色组非空输入最大字符验证"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "角色管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "角色管理", "span", 2)

        logger.info("点击创建角色组")
        Common.touch_by_id(self, ID.showAddRoleGroupModalBtn)

        logger.info("在角色组名为空时保存")
        Common.touch_by_id(self, ID.attendModelOkBtn)

        logger.info("无法保存提示不能为空")
        err_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, err_list, "请输入角色组名称"))

        logger.info("查看是否有输入长度限制")
        input_ele = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "角色组名称")
        self.assertEqual(input_ele.get_attribute("maxlength"), "10")


