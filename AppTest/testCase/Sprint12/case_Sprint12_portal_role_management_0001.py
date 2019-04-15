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
        u"""管理端-角色管理页面整体显示"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "角色管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "角色管理", "span", 2)

        logger.info("查看页面显示是否有遗漏")
        sear_1 = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "输入角色名称进行搜索")
        self.assertIsNotNone(sear_1)
        self.assertTrue(Common.check_if_id_exist(self, ID.showAddRoleGroupModalBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.showAddRoleModal))
        self.assertTrue(Common.check_if_id_exist(self, ID.setRoleRightsBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.editRoleBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.delRoleBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.addUserToRoleBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.outportRoleDataBtn))
