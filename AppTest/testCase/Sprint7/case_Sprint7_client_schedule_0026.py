#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.del_sechdule_by_name(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""日程编辑界面编辑日程内容"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "服务")
        Common.wait(self, 2)

        logger.info("点击任务")
        Common.touch_text_by_class_name(self, ClassName.center, "日程")

        logger.info("判断是否进入日程界面")
        text = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")[-1]
        self.assertEqual(text, "日程")

        logger.info("点击创建一个日程")
        Common.creat_schedule(self, "schedule_11")

        logger.info("点击编辑")
        Common.touch_del_or_edit_by_sechedule_name(self, "schedule_11")

        logger.info("判断是否进入编辑界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        res1 = Common.check_text_in_list(self, text_list, "编辑日程")
        self.assertTrue(res1)

        logger.info("修改日程内容")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入日程内容", "new_schesjdadkls")
        Common.touch_by_id(self, ID.submitAddScheduleBtn)

        logger.info("判断是否修改成功")
        name = Common.get_text_by_class_name(self, ClassName.schedule_item_name_ivu_col_span_14, "div")
        rest1 = Common.check_text_in_list(self, name, "new_schesjdadkls")
        self.assertTrue(rest1)


