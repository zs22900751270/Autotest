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
        u"""新建任务，抄送人选择框名称"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("点击新建任务,选择不提醒")
        Common.touch_by_id(self, ID.createTask)

        logger.info("点击添加抄送人")
        copy_ele = Common.get_result_by_class_name_blank(self, "section", ClassName.task_copy)
        Common.touch_tag_name_by_element(self, copy_ele, "li")

        logger.info("判断是否进入添加抄送人界面")
        copy_name = Common.get_text_by_class_name(self, ClassName.ivu_modal_header, "div")
        res = Common.check_text_in_list(self, copy_name, "请选择抄送人")
        self.assertTrue(res)


 
    
