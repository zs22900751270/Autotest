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
        Common.delete_role_group_by_name(self, "zs_group")
        Common.delete_role_group_by_name(self, "new_group")
        Common.quit(self)

    def test_step(self):
        u"""管理端-角色管理-角色组重命名显示验证"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "角色管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "角色管理", "span", 2)

        logger.info("点击创建角色组")
        Common.touch_by_id(self, ID.showAddRoleGroupModalBtn)

        logger.info("输入角色组名保存")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "角色组名称", "zs_group")
        Common.touch_by_id(self, ID.attendModelOkBtn)

        logger.info("查看是否创建成功")
        title_list = Common.get_text_by_class_name(self, ClassName.ivu_menu_submenu_title, "div")
        self.assertTrue(Common.check_text_in_list(self, title_list, "zs_group"))

        logger.info("点击编辑，进行重命名")
        name_list = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_menu_submenu_title, "zs_group")
        Common.touch_id_by_element(self, ID.renameRoleGroupBtn, name_list)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "角色组名称", "new_group")
        Common.touch_by_id(self, ID.attendModelOkBtn)

        logger.info("查看重命名是否成功")
        title_list = Common.get_text_by_class_name(self, ClassName.ivu_menu_submenu_title, "div")
        self.assertTrue(Common.check_text_in_list(self, title_list, "new_group"))


