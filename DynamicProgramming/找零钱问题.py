# -*- coding: utf-8 -*-
# @Time    : 10/27/20 9:37 AM
# @Author  : Yippee Song
# @Software: PyCharm
'''
k 中面值的硬币，面值分别是c1,c2,...,ck
问，至少需要多少枚硬币可以凑出 amount，如果不能凑出，则返回-1

'''

import math


class Solution(object):

    def dpSolution(self, coins, amount):
        dic = {i: float('inf') for i in range(amount + 1)}
        dic[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    break
                dic[i] = min(dic[i], 1 + dic[i - c])
        return -1 if math.isinf(dic[amount]) else dic[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 1001
    print Solution().dpSolution(coins, amount)
