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
        BaseOperate.quit(self)

    def test_step(self):
        u"""android—拍照设置头像功能正常可用"""
        logger.info("打开App")
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("点击进行登录")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touchById(self, PhoneControl.id_me_icon)

        logger.info("进入我的头像")
        BaseOperate.touchById(self, PhoneControl.id_profile_layout)

        logger.info("点击选择图片")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "拍照")

        logger.info("允许访问摄像头")
        while BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touchById(self, PhoneControl.id_permission_allow_button)
            BaseOperate.wait(self, 2)

        logger.info("判断是否打开摄像头")
        result = BaseOperate.checkIfIdExist(self, PhoneControl.id_shutter_button)
        self.assertTrue(result)



    
