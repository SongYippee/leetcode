# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 09:06
# @Author  : Yippee Song
# @Software: PyCharm
'''

509 斐波那契数列
'''


class Solution(object):
    def __init__(self):
        self.book = {0: 0, 1: 1}

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N not in self.book:
            self.book[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.book[N]