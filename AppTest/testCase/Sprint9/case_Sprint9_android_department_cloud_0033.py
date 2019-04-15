#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
my_folder_name = "zs_test"


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
        BaseOperate.del_dept_cloud_file_by_user_and_file(self, Content.register_count, my_folder_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-部门云盘-云盘操作-新建文件夹"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("点击首页, 进入云盘")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_homeLayout)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_yunpan)

        logger.info("判断是否进入云盘界面")
        text_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv)
        self.assertEqual(text_1, "云盘")

        logger.info("进入云盘节点")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_dept_files)

        logger.info("判断是否进入云盘节点")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "云盘节点")

        logger.info("进入组织云盘")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_title)

        logger.info("判断是否进入组织云盘")
        self.assertEqual(BaseOperate.get_text_by_id(self, PhoneControl.id_toolbar_title_tv), "组织云盘")

        logger.info("创建文件夹")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_new_folder)
        BaseOperate.sendTextById(self, PhoneControl.id_remark, my_folder_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_toolbar_right_tv)

        logger.info("判断是否创建成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, my_folder_name))


 
     
