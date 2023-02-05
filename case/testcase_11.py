"""
案例练习，测试tools模块add函数
"""
import unittest

from learn_01.tools import add


class TestAdd(unittest.TestCase):
    def test_01(self):
        if add(1,2) == 3:
            print("测试通过")
        else:
            print("测试不通过")

    def test_02(self):
        if add(3,4) == 7:
            print("测试通过")
        else:
            print("测试不通过")

    def test_03(self):
        if add(11,22) == 33:
            print("测试通过")
        else:
            print("测试不通过")