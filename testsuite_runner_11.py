import unittest

from learn_01.case.testcase_11 import TestAdd
# 实例化suite套件对象
suite = unittest.TestSuite()
# 添加测试方法
suite.addTest(TestAdd('test_01'))
suite.addTest(TestAdd('test_02'))
suite.addTest(TestAdd('test_03'))

# 实例化runner执行对象
runner = unittest.TextTestRunner()
runner.run(suite)