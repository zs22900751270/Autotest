#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64, requests, json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from AppTest.Common.Common import *


class Interface:

    def __init__(self):
        """"""

    def get_client_login_info(self, login_count, login_password):
        """"""
        public_key = requests.get(Interface_con.public_key)
        j_text = json.loads(public_key.text)
        rsaId = j_text["data"]["id"]
        pubkey = j_text["data"]["pubkey"]
        fin_key = "-----BEGIN PUBLIC KEY-----\n" + pubkey + "\n-----END PUBLIC KEY-----"
        rsakey = RSA.importKey(fin_key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(bytes(login_password, "utf-8")))
        cipher_text1 = str(cipher_text, encoding="utf-8")
        user_data = '{"phone": "%s", ' \
                    '"password": "%s", ' \
                    '"code": "", ' \
                    '"rsaId": "%s"}' % (login_count, cipher_text1, rsaId)
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "source": "webclient",
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
        }
        user_info = requests.post(Interface_con.client_login, data=user_data, headers=header)
        user_info_json = json.loads(user_info.text)
        return user_info_json["data"]

    def get_protal_login_info(self, login_count, login_password):
        """"""
        public_key = requests.get(Interface_con.public_key)
        j_text = json.loads(public_key.text)
        rsaId = j_text["data"]["id"]
        pubkey = j_text["data"]["pubkey"]
        fin_key = "-----BEGIN PUBLIC KEY-----\n" + pubkey + "\n-----END PUBLIC KEY-----"
        rsakey = RSA.importKey(fin_key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(bytes(login_password, "utf-8")))
        cipher_text1 = str(cipher_text, encoding="utf-8")
        user_data = '{"code": "", ' \
                    '"password": "%s", ' \
                    '"phone": "%s", ' \
                    '"rsaId": "%s"}' % (cipher_text1, login_count, rsaId)
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "source": "webadmin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
        }
        user_info = requests.post(Interface_con.protal_login, data=user_data, headers=header)
        user_info_json = json.loads(user_info.text)
        return user_info_json["data"]

    def modify_phone_num(self, old_phone, old_password, new_phone):
        """"""
        user_data = Interface.get_protal_login_info(self, old_phone, old_password)
        url_1 = "https://api.cnhqd.net/userManager/userInfo/getVerifyCode?phone={}&type=3".format(new_phone)
        requests.get(url_1)
        ident_code = Common.get_identifying_code(self, new_phone)
        s_id = Common.get_info_by_sql(self, "SELECT id FROM user WHERE phone='%s'" % old_phone, "scap")
        url_2 = "https://api.cnhqd.net/userManager/userInfo/updatePhone"
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": "jwt " + user_data["accessToken"],
            "source": "webadmin",
            "s_id": s_id,
        }
        modify_data = '{"phone": "%s", "type": 3, "verifyCode": "%s"}' % (new_phone, ident_code)
        requests.post(url_2, data=modify_data, headers=header)


