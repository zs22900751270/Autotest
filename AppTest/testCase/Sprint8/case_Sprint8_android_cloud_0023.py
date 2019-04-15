#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
long_name = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn" \
            "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"


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
        BaseOperate.del_cloud_file_by_user(self, Content.register_count)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓新建文件夹长度"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入云盘, 打开上传界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_my_files)

        logger.info("创建文件夹")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, long_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv, t=0)
        self.assertTrue(BaseOperate.find_toast(self, "文件名不能超过50个汉字"))


 
     
