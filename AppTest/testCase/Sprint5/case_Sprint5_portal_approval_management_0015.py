#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
group_name = "auto_test"
approval_name = "sprint5_15"
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
        logger.info("删除已创建的审批")
        Common.connect_sql(self, "DELETE FROM proc_classify WHERE name='%s'" % group_name, "scap")
        Common.connect_sql(self, "DELETE FROM proc_info WHERE NAME LIKE '%s'" % approval_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""审批图标选择"""
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



    
