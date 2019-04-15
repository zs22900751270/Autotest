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
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""新建任务，结束时间必须大于开始时间"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("点击新建任务")
        Common.touch_by_id(self, ID.createTask)

        logger.info("输入创建任务的参数")
        now = datetime.datetime.now()
        format_time = now + datetime.timedelta(minutes=50)
        start_time = datetime.datetime.strftime(format_time, "%Y-%m-%d %H:%M:%S")
        format_time = now + datetime.timedelta(minutes=40)
        end_time = datetime.datetime.strftime(format_time, "%Y-%m-%d %H:%M:%S")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mission_content")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_by_link_text(self, "指派给自己")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不提醒", "li")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("创建失败")
        text_lsit = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, text_lsit, "结束时间不能早于开始时间"))


 
    
