#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
folder_name = ".aaaaaa"
file_name = "zhangsen_1K"


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
        BaseOperate.clear_android_local_file(self, folder_name)
        BaseOperate.del_dept_cloud_file_by_user_and_file(self, Content.register_count, file_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""安卓-部门云盘-部门云盘角色权限控制-部门员工-自己所属文件夹可操作按钮验证"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录账号密码")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("创建一个大小为1K的文件")
        BaseOperate.creat_file_from_window_to_android(self, file_name, folder_name, 1024)

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

        logger.info("上传一个文件")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        if BaseOperate.checkIfIdExist(self, PhoneControl.id_permission_allow_button):
            BaseOperate.touch_id_by_index(self, PhoneControl.id_permission_allow_button)
            BaseOperate.touch_id_by_index(self, PhoneControl.id_upload_file)
            BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, "文件")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, folder_name)

        logger.info("选择文件开始上传")
        BaseOperate.touch_text_by_class_name(self, PhoneControl.class_name_TextView, file_name)
        BaseOperate.touch_id_by_index(self, PhoneControl.id_btn_addbook)

        logger.info("判断是否上传成功")
        name_list = BaseOperate.get_text_list_by_id(self, PhoneControl.id_name)
        self.assertTrue(BaseOperate.check_text_in_list(self, name_list, file_name))


 
     
