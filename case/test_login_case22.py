import unittest

from learn_01.tools import login


class TestLogin(unittest.TestCase):
    def testlogin_1(self):
        """正确的用户名和密码-admin，123456"""
        self.assertEqual('登陆成功',login('admin','123456'))

    def testlogin2(self):
        """错误的用户名和密码-root，123456"""
        self.assertEqual('登陆失败',login('root','123456'))

    def testlogin3(self):
        """错误的用户名和密码-admin，123123"""
        self.assertEqual('登陆失败',login('admin','123123'))

    def testlogin4(self):
        """错误的用户名和密码-aaa，123123"""
        self.assertEqual('登陆失败',login('aaa','123123'))