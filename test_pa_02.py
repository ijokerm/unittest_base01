"""
代码演示：
1.导包
2.定义测试类
3.书写测试方法（用到的测试数据使用变量代替）
4.组织测试数据并传参 --装饰器@parameterized.expand(data)
"""
import json
import unittest
from parameterized import parameterized

from learn_01.tools import login
# 组织测试数据 --注意顺序要和参数的位置保持一致
def get_data():
    with open('data.json', encoding='UTF-8') as f:
        result = json.load(f)
        data = []
        for i in result:
            data.append((i.get('username'), i.get('password'), i.get('expect')))

        return data

class TestLogin(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_login(self,username,password,expect):
        self.assertEqual(expect,login(username,password))

