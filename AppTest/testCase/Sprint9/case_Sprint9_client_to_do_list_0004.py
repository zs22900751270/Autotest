#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.del_sechdule_by_name(self, Content.register_count)
        Common.delete_meeting_record(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""待办界面所有事件都可以点击查看详情"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("清空待办列表")
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.del_sechdule_by_name(self, Content.register_count)
        Common.delete_meeting_record(self, Content.register_count)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("创建多个任务")
        Common.touch_by_id(self, ID.taskBtn)
        Common.creat_mission(self, "mission_content_1")
        Common.creat_mission(self, "mission_content_2")
        Common.creat_mission(self, "mission_content_3")

        logger.info("点击进入待办界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "服务")
        Common.touch_by_id(self, ID.todoBtn)

        logger.info("查看是否进入待办界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link)
        self.assertTrue(Common.check_text_in_list(self, text_list, "待办"))

        logger.info("点击进入待办详情1")
        list_wrap = Common.get_result_by_class_name(self, ClassName.list_wrap)
        h5_ele = Common.get_tag_name_by_element(self, list_wrap, "h5", None)
        Common.touch_text_by_elements(self, h5_ele, "mission_content_1")
        logger.info("查看是否进入事件详情界面")
        detail_1 = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(BaseOperate.check_text_in_list(self, detail_1, "任务详情"))
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "服务")
        Common.touch_by_id(self, ID.todoBtn)

        logger.info("点击进入待办详情2")
        list_wrap = Common.get_result_by_class_name(self, ClassName.list_wrap)
        h5_ele = Common.get_tag_name_by_element(self, list_wrap, "h5", None)
        Common.touch_text_by_elements(self, h5_ele, "mission_content_2")
        logger.info("查看是否进入事件详情界面")
        detail_1 = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(BaseOperate.check_text_in_list(self, detail_1, "任务详情"))
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "服务")
        Common.touch_by_id(self, ID.todoBtn)

        logger.info("点击进入待办详情3")
        list_wrap = Common.get_result_by_class_name(self, ClassName.list_wrap)
        h5_ele = Common.get_tag_name_by_element(self, list_wrap, "h5", None)
        Common.touch_text_by_elements(self, h5_ele, "mission_content_3")
        logger.info("查看是否进入事件详情界面")
        detail_1 = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")
        self.assertTrue(BaseOperate.check_text_in_list(self, detail_1, "任务详情"))

