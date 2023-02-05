"""
代码演示：
1.导包
2.定义测试类
3.书写测试方法（用到的测试数据使用变量代替）
4.组织测试数据并传参 --装饰器@parameterized.expand(data)
"""
import unittest
from parameterized import parameterized

from learn_01.tools import login
# 组织测试数据 --注意顺序要和参数的位置保持一致
data = [
    ('admin','123456','登陆成功'),
    ('root','123456','登陆失败'),
    ('admin','123123','登陆失败'),
    ('aaa','123123','登陆失败')
]

class TestLogin(unittest.TestCase):

    @parameterized.expand(data)
    def test_login(self,username,password,expect):
        self.assertEqual(expect,login(username,password))

