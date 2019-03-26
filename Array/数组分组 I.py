# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 11:29
# @Author  : Yippee Song
# @Software: PyCharm
'''
561 Array Partition I,
对长度为2N的数组分成 N 组，取每组中的最小值，然后使得这 N个值的和最大。
'''


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
