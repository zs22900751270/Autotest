#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
phoneNum = Content.register_count
password = Content.login_password
no_register_count = Content.no_register_count


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
        u"""忘记密码超长11位字符或短，或没有注册手机号码"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("进入忘记密码界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.me)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_or_register)
        BaseOperate.touch_id_by_index(self, PhoneControl.login_forget_password)
        # 在手机号码框输入超过11位手机号码
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, phoneNum + "123")
        # 只能输入11位
        reslut_input_num_1 = BaseOperate.get_text_by_id(self, PhoneControl.id_tel_num)
        # 判断是否可以输入
        self.assertTrue(len(reslut_input_num_1) == 11)

        # 输入少于11位手机号码
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, phoneNum[:-1])
        # 只能输入11位
        reslut_input_num_2 = BaseOperate.get_text_by_id(self, PhoneControl.id_tel_num)
        # 判断是否可以输入
        reslut_text = BaseOperate.get_text_by_id(self, PhoneControl.id_warning_tv)
        self.assertTrue(len(reslut_input_num_2) <= 11)
        self.assertTrue(reslut_text == "请输入11位电话号码")

        # 输入未注册手机号码
        BaseOperate.sendTextById(self, PhoneControl.id_tel_num, no_register_count)
        # 点击发送验证码
        BaseOperate.touch_id_by_index(self, PhoneControl.id_verify_code_btn, t=0)
        # 判断是否可以输入
        reslut_statue = BaseOperate.find_toast(self, "此账号不存在，请注册")
        self.assertTrue(reslut_statue)



    
