""""
演示报告生成
1.获取第三方的测试运行类模块，将其放在代码的目录中
2.导包 unittest
3.使用套件对象，加载对象去添加用例方法
4.使用第三方的运行对象 实例化对象 并运行套件对象
"""
import unittest
from HTMLTestRunnerCN import HTMLTestReportCN

suite = unittest.TestLoader().discover('./case','test_login_case22.py')

# stream=sys.stdout,必填， 测试报告的文件对象（open） --注意：使用wb打开
# verbosity=1, 可选，报告的详细程度，默认1，简略 2，详细
# title=None, 可选，报告的标题
# description=None ，可选，报告的描述信息 比如版本信息
# tester=None, 可选，测试人员
file = 'Creport.html'
with open(file,'wb') as f:
    runner = HTMLTestReportCN(f,1,'TestCase_02测试报告','Python3.11','SpringBear')

    runner.run(suite)


