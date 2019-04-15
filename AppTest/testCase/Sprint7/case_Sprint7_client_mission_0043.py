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
        u"""新建任务，执行人可以指派给自己或者其他通讯录中的人，且只能指派一个"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("点击新建任务,指派给其他人")
        Common.touch_by_id(self, ID.createTask)
        start_time = Common.get_mission_start_time(self)
        end_time = Common.get_mission_end_time(self)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mission_content")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择开始时间", start_time)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请选择结束时间", end_time)
        choice = Common.get_result_by_class_name_blank(self, "i", ClassName.ivu_icon_plus_circled_icon_normal)
        Common.touch_by_element(self, choice)
        executor_ele = Common.get_results_by_class_name_blank(self, "label",
                                                              ClassName.ivu_checkbox_wrapper_group_item)[0]
        Common.touch_by_element(self, executor_ele)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择", "span")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "不提醒", "li")

        logger.info("切换执行人为自己")
        Common.touch_by_link_text(self, "指派给自己")

        logger.info("点击保存")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("判断是否创建成功，且执行人为自己")
        name = Common.get_info_by_sql(self, "select realname from user where phone='%s'" % Content.register_count,
                                      "scap")
        text_list = Common.get_text_by_class_name(self, ClassName.task_item_detail, "div")
        res = Common.check_text_in_list(self, text_list, name)
        self.assertTrue(res)


 
    
