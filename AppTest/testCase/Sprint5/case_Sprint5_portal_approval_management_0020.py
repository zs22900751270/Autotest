#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
group_name = "auto_test"
approval_name = "sprint5_20"


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
        logger.info("删除已创建的审批")
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='%s'" % group_name, "scap")
        Common.connect_sql(self, "DELETE FROM proc_info WHERE NAME LIKE '%s'" % approval_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""删除审批流程"""
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
        fin_result = Common.check_approval_in_group(self, approval_name, group_name)
        self.assertTrue(fin_result)
        Common.wait(self, 3)

        logger.info("点击保存并发布")
        Common.touch_add_process_by_approval_name(self, approval_name)
        fr_id = Common.get_result_by_id(self, "modeler-iframe")
        Common.switch_to_frame(self, fr_id)
        Common.wait(self, 5)

        savebtn = Common.get_results_by_class_name_blank(self, "button", ClassName.btn_inverse_ng_scope)[0]
        Common.touch_by_element(self, savebtn)
        Common.wait(self, 1)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary_ng_scope, "保存并发布", "button")
        exist_result = Common.check_approval_in_group(self, approval_name, group_name)
        self.assertTrue(exist_result)



    
