#coding:utf-8

import unittest
import time

class Test(unittest.TestCase):

    def setUp(self):
        print("start!")
    def tearDown(self):
        time.sleep(1)
        print("end!")

    def testab(self):
        print("执行测试用例ab")
    def testaa(self):
        print("执行测试用例aa")
    def testcc(self):
        print("执行测试用例cc")
    def testbb(self):
        print("执行测试用例bb")
    def test02(self):
        print("执行测试用例02")
    def addtest(self):
        print("add方法")
    def test01(self):
        print("执行测试用例01")
    def test03(self):
        print("执行测试用例03")

if __name__ == '__main__':
    unittest.main()