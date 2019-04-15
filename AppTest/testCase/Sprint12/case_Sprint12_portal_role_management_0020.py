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
        Common.delete_role_group_by_name(self, "zs_role")
        Common.quit(self)

    def test_step(self):
        u"""管理端-角色管理-编辑按钮验证"""
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

        logger.info("创建新角色")
        Common.touch_by_id(self, ID.showAddRoleModal)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "角色名称", "zs_role")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "zs_group", "li")
        ele_input = Common.get_result_by_class_name_blank(self, "textarea", ClassName.ivu_input)
        Common.send_text_by_element(self, ele_input, "describe")
        Common.touch_by_id(self, ID.addRoleBtn)

        logger.info("查看是否创建成功")
        name_list = Common.get_element_by_class_name_and_text(self, "div", ClassName.ivu_menu_submenu_title, "zs_group")
        fol = Common.get_class_name_elements_by_element_blank(self, name_list, "i", ClassName.ivu_icon_ios_folder)
        Common.touch_by_element(self, fol[0])
        role_name = Common.get_text_by_class_name(self, ClassName.ivu_menu_item, "li")
        self.assertTrue(Common.check_text_in_list(self, role_name, "zs_role"))

        logger.info("点击进入角色界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "zs_role", "li")
        Common.touch_by_id(self, ID.setRoleRightsBtn)
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_modal_header_inner)
        self.assertTrue(Common.check_text_in_list(self, text_list, "设置角色权限"))

