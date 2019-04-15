#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)
        BaseOperate.del_friend_request_by_sql(self, Content.spare_count)
        BaseOperate.quit(self)

    def test_step(self):
        u"""在通讯录界面搜索好友"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("清除好友信息")
        BaseOperate.del_friend_by_sql(self, Content.register_count, Content.spare_count)

        logger.info("点击进行登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入通讯录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("点击添加")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("输入手机号码进行查找")
        BaseOperate.sendTextById(self, PhoneControl.id_search_edit, Content.spare_count)
        BaseOperate.touch_search_by_id(self, PhoneControl.id_search_edit)

        logger.info("点击添加")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_add)

        logger.info("输入好友验证信息")
        BaseOperate.sendTextById(self, PhoneControl.id_remark, "1234")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("退出登录")
        BaseOperate.app_login_out(self)

        logger.info("登录新的账号")
        BaseOperate.app_login(self, Content.spare_count, Content.spare_password)

        logger.info("进入通讯录界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_btn)

        logger.info("进入新朋友，点击确定")
        friend_name = BaseOperate.get_realname_by_phone(self, Content.register_count)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_friend)
        BaseOperate.except_friend_requset_or_not(self, friend_name, False)

        logger.info("判断添加好友是否成功")
        result = BaseOperate.check_add_friend_result(self, friend_name, False)
        self.assertTrue(result)



    
