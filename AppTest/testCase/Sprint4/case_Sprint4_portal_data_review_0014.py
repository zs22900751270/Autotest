#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


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
        Common.quit(self)

    def test_step(self):
        u"""数据表管理界面分页显示"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据审核管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据表管理")
        Common.wait(self, 3)

        logger.info("判断数据是否有分页")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_selected_value, "10 条/页", "span")

        logger.info("判断分页方式")
        page_result = Common.get_text_by_class_name(self, ClassName.ivu_select_dropdown_list, "ul")
        g_res_1 = Common.check_text_in_list(self, page_result, "10 条/页")
        g_res_2 = Common.check_text_in_list(self, page_result, "20 条/页")
        g_res_3 = Common.check_text_in_list(self, page_result, "30 条/页")
        g_res_4 = Common.check_text_in_list(self, page_result, "40 条/页")
        self.assertTrue(g_res_1)
        self.assertTrue(g_res_2)
        self.assertTrue(g_res_3)
        self.assertTrue(g_res_4)



    
