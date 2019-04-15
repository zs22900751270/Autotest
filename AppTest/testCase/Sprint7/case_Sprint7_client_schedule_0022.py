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
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.del_sechdule_by_name(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""日程列表显示"""
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
        Common.touch_by_id(self, ID.toAddScheduleBtn)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入日程内容", "schedule_content")
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不提醒", "li")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不重复", "li")
        Common.touch_by_id(self, ID.submitAddScheduleBtn)

        logger.info("获取时间")
        sechdule_list = Common.get_text_by_class_name(self, ClassName.schedule_item_name_col_span_2, "div")
        res1 = Common.check_text_in_list(self, sechdule_list, start_time[-8:-3])
        res2 = Common.check_text_in_list(self, sechdule_list, end_time[-8:-3])
        self.assertTrue(res1)
        self.assertTrue(res2)


