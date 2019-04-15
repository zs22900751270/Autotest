#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
group_name = "auto_test"
approval_name = "sprint5_11"
all_num = 2


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
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='%s'" % group_name, "scap")
        Common.connect_sql(self, "DELETE FROM proc_info WHERE NAME LIKE '%s'" % approval_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""在已停用中启用流程"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击内置应用")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "审批管理", "span", 2)

        logger.info("点击创建分组")
        Common.creat_new_group(self, group_name)

        logger.info("点击创建审批")
        Common.creat_approval(self, group_name, approval_name)

        logger.info("启用停用流程")
        Common.stop_approval_by_name(self, approval_name)

        logger.info("该分组中的审批是否移动至已停用")
        fin_result_1 = Common.check_approval_in_group(self, approval_name, "已停用")
        self.assertTrue(fin_result_1)
        Common.wait(self, 3)

        logger.info("在已停用中启用流程，该流程会恢复到之前分组")
        div_list = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_col_span_12)
        for group_name1 in div_list:
            group_name_list = Common.get_class_name_elements_by_element_blank(self, group_name1, "div",
                                                                              ClassName.item_content_c)[0]
            if approval_name in group_name_list.text:
                para = group_name1
                break
        result1 = Common.get_class_name_elements_by_element_blank(self, para, "button",
                                                                 ClassName.ivu_vtn_info_small)[0]
        Common.touch_by_element(self, result1)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.wait(self, 3)
        fin_result = Common.check_approval_in_group(self, approval_name, group_name)
        self.assertTrue(fin_result)



    
