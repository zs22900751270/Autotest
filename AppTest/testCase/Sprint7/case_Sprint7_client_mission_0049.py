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
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""新建任务，设置提醒可以设置为提前一小时、3小时、1天和不提醒"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)
        Common.wait(self, 2)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("点击新建任务,选择不提醒")
        Common.touch_by_id(self, ID.createTask)
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mission_no_remind")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_by_link_text(self, "指派给自己")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不提醒", "li")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("点击新建任务,选择截止前1小时提醒")
        Common.touch_by_id(self, ID.createTask)
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mission_one_hour")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_by_link_text(self, "指派给自己")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "截止前1小时", "li")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("点击新建任务,选择截止前3小时提醒")
        Common.touch_by_id(self, ID.createTask)
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mission_three_hours")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_by_link_text(self, "指派给自己")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "截止前3小时", "li")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("点击新建任务,选择截止前1天提醒")
        Common.touch_by_id(self, ID.createTask)
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mission_one_day")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        Common.touch_by_link_text(self, "指派给自己")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "截止前1天", "li")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("判断是否创建成功，且执行人为自己")
        task_name_list = Common.get_text_by_class_name(self, ClassName.task_item_name, "div")
        task_name_list = list(filter(None, task_name_list))
        self.assertEqual(len(task_name_list), 4)


 
    
