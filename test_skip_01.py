"""
演示跳过：
直接将测试函数标记成跳过
@unittest.skip('跳过原因')
根据条件判断测试函数是否跳过
@unittest.skipIf(判断条件,'跳过原因')
"""
import unittest

version = 10

class TestDemo(unittest.TestCase):
    @unittest.skip('测试跳过-skip ')
    def test_1(self):
        print("测试方法 1")
    @unittest.skipIf(version >= 30,'版本大于等于30无需测试')
    def test_2(self):
        print("测试方法 2")

    def test_3(self):
        print("测试方法 3")