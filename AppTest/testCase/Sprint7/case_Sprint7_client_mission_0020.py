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
        u"""未完成的页面按照更新时间排序"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)
        Common.wait(self, 2)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("创建多个任务")
        for i in range(5):
            Common.creat_mission(self, "mission_content%s" % i)
            Common.wait(self, 2)

        logger.info("将所创建任务标记已完成")
        for i in range(5):
            logger.info("标记任务已完成")
            Common.open_mission_detail_by_name(self, "mission_content%s" % i, Content.register_count)
            Common.touch_by_id(self, ID.setTaskFinishBtn)
            Common.wait(self, 2)
            Common.back(self)
            Common.wait(self, 3)

        logger.info("获取所有任务状态")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "已完成的")
        name_list = Common.get_text_by_class_name(self, ClassName.task_status_undone, "span")
        name_list = list(filter(None, name_list))

        logger.info("判断任务排序是否相同")
        for i in name_list:
            self.assertEqual(i, "已完成")


