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
        Common.modify_user_locked_status_by_phone(self, Content.spare_count)
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""管理端-启用后用户列表信息刷新验证"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 2)

        logger.info("搜索账号进行禁用")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入账号或姓名进行搜索",
                                                       Content.spare_count+"\n")

        logger.info("点击禁用")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_ghost_small, "禁用", "button")

        logger.info("查看是否出现禁用原因输入框")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_modal_header_inner, "div")
        self.assertTrue(Common.check_text_in_list(self, text_list, "请输入禁用原因"))

        logger.info("输入禁用原因，禁用该用户")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入原因", "ju_jue")
        Common.touch_by_id(self, ID.attendModelOkBtn)

        logger.info("查看用户状态是否变化")
        user_statue = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_table_cell, "禁用")
        self.assertEqual(user_statue.text, "禁用")

        logger.info("点击启用")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_ghost_small, "启用", "button")

        logger.info("查看是否出现启用原因输入框")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_modal_header_inner, "div")
        self.assertTrue(Common.check_text_in_list(self, text_list, "请输入启用原因"))

        logger.info("输入禁用原因，禁用该用户")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入原因", "qi_yong")
        Common.touch_by_id(self, ID.attendModelOkBtn)

        logger.info("查看用户状态是否变化")
        user_statue = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_table_cell, "启用")
        self.assertEqual(user_statue.text, "启用")

