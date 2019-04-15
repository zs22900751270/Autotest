#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
phoneNum = Content.register_count
password = Content.login_password


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        self.driver = deviceDriver.mydriver(self)
        BaseOperate.installApp(self, Content.app_name)

    @classmethod
    def tearDown(self):
        BaseOperate.report_screen_shot(self, self.case_name)
        BaseOperate.uninstallApp(self, PhoneControl.package_name)
        BaseOperate.quit(self)

    def test_step(self):
        u"""个人资料和后台保持一致"""
        BaseOperate.startActivity(self, PhoneControl.package_name, PhoneControl.activity_name)

        logger.info("登录app")
        BaseOperate.app_login(self, Content.register_count, Content.login_password)

        logger.info("进入我的资料界面")
        BaseOperate.touch_id_by_index(self, PhoneControl.id_me_icon)

        logger.info("从前台获取信息")
        Qtinfo = []
        name = BaseOperate.get_text_by_id(self, PhoneControl.id_nick_name)
        if name == "未填写":
            pass
        else:
            Qtinfo.append(name)
        realname = BaseOperate.get_text_by_id(self, PhoneControl.id_true_name)
        sex = BaseOperate.get_text_by_id(self, PhoneControl.id_sex)
        if sex == "男":
            sex = "0"
        elif sex == "女":
            sex = "1"
        birthday = BaseOperate.get_text_by_id(self, PhoneControl.my_data_birthday)
        mail = BaseOperate.get_text_by_id(self, PhoneControl.id_mail)
        Qtinfo.append(realname)
        Qtinfo.append(sex)
        Qtinfo.append(birthday)
        Qtinfo.append(mail)

        logger.info("从后台获取信息")
        HtInfo = Ldap.ldap_cn_list(self, "user", "ou=users", "cn=%s" % Content.register_count)
        HTinfo = str(HtInfo[0])
        j = 0
        for i in Qtinfo:
            if i in HTinfo:
                logger.info("'%s'存在于后台信息中" % i)
                pass
            else:
                logger.info("'%s'不存在于后台信息中" % i)
                logger.info(j)
                j += 1
        self.assertEqual(j, 0)




