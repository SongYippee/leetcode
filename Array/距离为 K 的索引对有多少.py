# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 16:59
# @Author  : Yippee Song
# @Software: PyCharm

from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k < 0:
            return 0
        else:
            if k == 0:
                cnt = 0
                for k, v in Counter(nums).items():
                    if v >= 2:
                        cnt += 1
                return cnt
            else:
                '''
                集合的交集 可以用&符号计算
                '''
                return len(set(nums) & set(n + k for n in nums))
