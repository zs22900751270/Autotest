#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
group_name = "aA!@#$123"
group_name_new = "zhangsen"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        logger.info("清除所创建的数据")
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='aA!@#$123'", "scap")
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='zhangsen'", "scap")
        Common.quit(self)

    def test_step(self):
        u"""审批管理界面新建审批分组"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.wait(self, 2)

        logger.info("点击新建分组")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 2)
        aa = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_ghost)
        Common.touch_by_element(self, aa)

        logger.info("判断分组名称长度")
        name_len = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "请输入分组名称")
        name_len_1 = name_len.get_attribute("maxlength")
        self.assertTrue(name_len_1 == "20")

        logger.info("输入分组名称为啊aA!@#$123的分组")
        Common.send_text_by_element(self, name_len, "aA!@#$123")
        ok_but = Common.get_result_by_class_name_blank(self, "button", ClassName.ivu_btn_large)
        Common.touch_by_element(self, ok_but)
        Common.wait(self, 3)

        logger.info("判断是否创建成功")
        get_group = Common.get_results_by_class_name(self, ClassName.group)
        get_group_text = Common.get_text_by_elements(self, get_group)
        get_result = Common.check_text_in_list(self, get_group_text, group_name)
        self.assertTrue(get_result)

        logger.info("点击编辑")
        Common.rename_group_by_name(self, "aA!@#$123", "zhangsen")

        logger.info("判断重命名成功")
        new_group1 = Common.get_element_by_class_name_and_text(self, "div", ClassName.group_list_ivu_row,
                                                               group_name_new)
        self.assertNotEqual(new_group1, False)



    
