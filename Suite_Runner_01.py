"""
套件和执行 演示：
1.导包
2.创建对象（实例化）
3.使用套件对象添加用例方法
方式一：套件对象.addTest(测试类名('方法名'))
方式二：套件对象.addTest(unittest.makeSuite(测试类名))
4.实例化运行对象
5.使用运行对象执行套件对象
"""
import unittest

from learn_01.case.TestCase_02 import TestDemo1
from learn_01.case.TestCase_03 import TestDemo2

suite = unittest.TestSuite()

suite.addTest(TestDemo1("test_method1"))
suite.addTest(TestDemo1('test_method2'))
suite.addTest(TestDemo2('test_method1'))
suite.addTest(TestDemo2('test_method2'))



runner = unittest.TextTestRunner()

runner.run(suite)