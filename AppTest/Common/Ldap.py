#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppTest.Driver.Phone_Driver import *
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE

"""
Ldap的操作方式
"""

ADMIN_DN = "dc=cnhqd,dc=com"
LDAP_IP = '114.116.46.120'
LDAP_port = 389
LDAP_user = "cn=root,dc=cnhqd,dc=com"
LDAP_pwd = '123456'


class Ldap:
    def __init__(self):
        """init function"""
        logger.info("初始化")

    @staticmethod
    def ldap_del(self, cnoudel):
        """
        ldap_del ; shan chu ldap shu ju
        :param cnoudel:
        :return:
        """
        server = Server(LDAP_IP, port=LDAP_port, get_info=ALL)
        conn = Connection(server, user=LDAP_user, password=LDAP_pwd)
        conn.open()
        conn.bind()
        conn.delete(cnoudel + "," + ADMIN_DN)
        conn.unbind()

    @staticmethod
    def ldap_list(self, obj_class, ou):
        """
        ldap_list
        :param obj_class:
        :param ou:
        :return: objlist
        """
        server = Server(LDAP_IP, port=LDAP_port, get_info=ALL)
        conn = Connection(server, user=LDAP_user, password=LDAP_pwd)
        conn.open()
        conn.bind()
        conn.search(ou + "," + ADMIN_DN, "(&(objectClass=" + obj_class + "))")
        objlist = conn.entries
        conn.unbind()
        return objlist

    @staticmethod
    def ldap_cn_list(self, obj_class, ou, cn):
        """
        ldap_cn_list
        :param obj_class: ldap 数据库中的信息
        :param ou: ldap 数据库中的信息
        :param cn: ldap yong hu xin xi
        :return: display
        """
        server = Server(LDAP_IP, port=LDAP_port, get_info=ALL)
        conn = Connection(server, user=LDAP_user, password=LDAP_pwd)
        conn.open()
        conn.bind()
        conn.search(ou + "," + ADMIN_DN, "(&(objectClass=" + obj_class + ")(" + cn + "))", attributes=["*"])
        display = conn.entries
        conn.unbind()
        return display

    def modify_attribute_by_name(self, cn, group_name, attribute, attribute_value):
        """
        modify attribute by phone
        :param phone:
        :param attribute:
        :param attribute_value:
        :return:
        """
        server = Server(LDAP_IP, port=LDAP_port, get_info=ALL)
        conn = Connection(server, user=LDAP_user, password=LDAP_pwd)
        conn.open()
        conn.bind()
        conn.modify("cn="+cn+",ou="+group_name+",dc=cnhqd,dc=com", {attribute: [(MODIFY_REPLACE, [attribute_value])]})
        conn.unbind()

