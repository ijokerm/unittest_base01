"""
TestLoader代码演示
1.导包
2.实例化加载对象并添加用例 --> 得到suite对象
unittest.TestLoader().discover('用例所在的路径','用例的代码文件名')
3.实例化 运行对象
4.运行对象执行 套件对象
"""
import unittest

suite = unittest.TestLoader().discover('./case', '*')
runner = unittest.TextTestRunner()

runner.run(suite)

