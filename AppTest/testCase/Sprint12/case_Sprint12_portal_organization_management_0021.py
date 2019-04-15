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
        Common.delete_department_by_name(self, "zs_test")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.quit(self)

    def test_step(self):
        u"""pc-添加部门批量删除成员"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "新建部门", "button")

        logger.info("输入一个存在与系统中的主管账号")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "新建部门", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入部门名称", "zs_test")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入部门主管手机号码",
                                                       Content.register_count)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("查看是否可以创建成功")
        department_name = Common.get_result_by_class_name(self, ClassName.department)
        name_ele_list = Common.get_class_name_elements_by_element(self, department_name, ClassName.name)
        name_list = Common.get_text_by_elements(self, name_ele_list)
        self.assertTrue(Common.check_text_in_list(self, name_list, "zs_test"))

        logger.info("点击添加人员")
        Common.touch_text_by_class_name(self, ClassName.name, "zs_test", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加人员", "button")
        header = Common.get_text_by_class_name(self, ClassName.ivu_modal_header_inner, "div")
        self.assertTrue(Common.check_text_in_list(self, header, "添加人员"))

        logger.info("添加第一个人员")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加人员", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号码",
                                                       Content.spare_count)
        ele = Common.get_results_by_class_name(self, ClassName.ivu_input)
        Common.send_text_by_element(self, ele[-1], "new_zhi_wei")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        logger.info("添加第二个人员")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加人员", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号码",
                                                       Content.spare_count1)
        ele = Common.get_results_by_class_name(self, ClassName.ivu_input)
        Common.send_text_by_element(self, ele[-1], "new_zhi_wei_1")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("查看是否添加成功")
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        real_name1 = Common.get_realname_by_phone(self, Content.spare_count1)
        name_list_1 = Common.get_text_by_class_name(self, ClassName.ivu_table_cell)
        self.assertTrue(Common.check_text_in_list(self, name_list_1, real_name))
        self.assertTrue(Common.check_text_in_list(self, name_list_1, real_name1))

        logger.info("点击全选,进行删除")
        all_sel = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_checkbox_input)[0]
        Common.touch_by_element(self, all_sel)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_warning, "删除人员", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("查看是否可以删除成功")
        real_name = Common.get_realname_by_phone(self, Content.spare_count)
        real_name1 = Common.get_realname_by_phone(self, Content.spare_count1)
        name_list_1 = Common.get_text_by_class_name(self, ClassName.ivu_table_cell)
        self.assertFalse(Common.check_text_in_list(self, name_list_1, real_name))
        self.assertFalse(Common.check_text_in_list(self, name_list_1, real_name1))
