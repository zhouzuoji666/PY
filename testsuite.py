
import unittest,time
import HTMLTestRunner
from 单元测试.test_math import test_math
#测试集
suite=unittest.TestSuite()
suite.addTest(test_math("test_add"))
suite.addTest(test_math("test_sub"))
#执行测试集
now=time.strftime('%Y-%m-%d_%H_%M_%S')#当前测试时间
filePath="测试报告"+now+"html"#路径
fp=open(filePath,"wb")
running=HTMLTestRunner.HTMLTestRunner(stream=fp,title="单元测试")#运行
running.run(suite)
fp.close()