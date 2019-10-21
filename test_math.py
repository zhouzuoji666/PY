#单元测试
import unittest
import parameterized as parameterized
from 单元测试.math import math

class test_math(unittest.TestCase):

    def setUp(self):
        print("测试开始")
    @parameterized.parameterized.expand([(1,2),(3,4),(5,6)])
    def test_add(self,a,b):
        try:
            t=math()
            result=t.add(a,b)
            self.assertEqual(result,3,"期望值不正确")
            print(result)
        except AssertionError as e:
            print("错误是：%s" % e)
            raise e
    @parameterized.parameterized.expand([(1, 2), (3, 4), (5, 6)])
    def test_sub(self,a,b):
        try:
            t=math()
            result=t.sub(a,b)
            self.assertEqual(result,-3,"期望值不正确")
            print(result)
        except AssertionError as e:
            print("错误是：%s"%e)
            raise e

    def tearDown(self):
        print("测试结束")