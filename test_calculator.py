# @Time : 2021/2/18 19:36
# @Author : DengZh
# @File : test_calculator.py
# @Software: PyCharm
from unittest import TestCase

from calculator import Calculator


class TestCalculator(TestCase):
    def test_add(self):
        # self.fail()
        self.calculator=Calculator()
        self.assertEqual(self.calculator.add(3,4),7)
    def test_multiply(self):
        self.fail()
