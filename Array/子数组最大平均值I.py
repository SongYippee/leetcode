# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:35
# @Author  : Yippee Song
# @Software: PyCharm
'''
643 Maximum Average Subarray I
'''


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxSum = sum(nums[0:k])
        temp = maxSum
        for i in range(k, len(nums)):
            temp += nums[i] - nums[i - k]
            maxSum = max(maxSum, temp)
        return float(maxSum) / k

