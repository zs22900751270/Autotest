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
        Common.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        Common.clear_mission_info_by_sql(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""被抄送人删除任务后，对任务进行操作"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("创建好友关系")
        Common.creat_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "任务", "p")

        logger.info("创建一个会议")
        realname = Common.get_realname_by_phone(self, Content.spare_count)
        Common.creat_mission(self, "mission_theme", copyer=realname)

        logger.info("登录抄送人账号")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "任务", "p")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "抄送我的")
        Common.open_mission_detail_by_name(self, "mission_theme", Content.register_count, 5)

        logger.info("点击删除按钮")
        Common.touch_by_id(self, ID.deteleTaskBtn)
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断是否删除成功")
        self.assertFalse(Common.check_mession_belong_to(self, "mission_theme", 5))

        logger.info("返回创建任务界面，查看该任务是否收到影响")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "任务", "p")

        logger.info("判断创建人的任务是否还在")
        self.assertTrue(Common.check_mession_belong_to(self, "mission_theme", 1))

        logger.info("进行编辑任务")
        Common.open_mission_detail_by_name(self, "mission_theme", Content.register_count, 1)
        Common.touch_by_id(self, ID.editTaskBtn)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入任务内容", "mes_content_new")
        Common.touch_by_id(self, ID.saveTaskBtn)

        logger.info("返回创建任务界面，查看该任务是否收到影响")
        Common.open_new_page_in_chrome(self, WebControl.web_url)
        Common.login_web_client(self, Content.spare_count, Content.spare_password)

        logger.info("点击进入服务界面")
        Common.touch_by_id(self, ID.toService)

        logger.info("进入会议界面")
        Common.touch_text_by_class_name(self, ClassName.center, "任务", "p")

        logger.info("进入抄送人账号，查看是否收到信息")
        Common.touch_text_by_class_name(self, ClassName.ivu_tabs_tab, "抄送我的")
        self.assertFalse(Common.check_mession_belong_to(self, "mes_content_new", 5))


 
     
