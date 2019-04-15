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
        u"""我发出的页面状态显示"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("创建多个任务")
        for i in range(5):
            Common.creat_mission(self, "mission_content%s" % i)

        logger.info("将部分任务标记已完成")
        for i in range(5):
            if i > 2:
                Common.open_mission_detail_by_name(self, "mission_content%s" % i, Content.register_count)
                Common.touch_by_id(self, ID.setTaskFinishBtn)
                Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "任务", "a")

        logger.info("获取所有任务状态")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "我发出的")

        logger.info("判断任务排序是否相同")
        done = Common.check_if_class_name_exist(self, ClassName.task_status_done, "span")
        undone = Common.check_if_class_name_exist(self, ClassName.task_status_undone, "span")
        self.assertTrue(done)
        self.assertTrue(undone)


 
    
