# -*- coding: utf-8 -*-
# @Time    : 10/27/20 4:59 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        if n > 2:
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
