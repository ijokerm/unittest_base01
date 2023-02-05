"""
学习TestCase模块书写方法
"""
# 1.导包
import unittest

# 2.自定义测试类 --需要继承unittest模块中的TestCase类
class TestDemo(unittest.TestCase):
    # 3.书写测试方法 --书写要求：必须以test_开头
    def test_method1(self):
        print("测试方法 1")

    def test_method2(self):
        print("测试方法 2")

# 4.执行用例（方法） --1：鼠标指向类名的后边运行(执行类中的所有测试方法) 2：在方法名后边运行(只执行当前方法)