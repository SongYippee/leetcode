# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 10:57
# @Author  : Yippee Song
# @Software: PyCharm
'''
697 Degree of an Array
找出非空非负数的数组 A中的子数组 A' 使得 A'的 degree和 A的 degree相同
'''


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, counter, ans, degree = {}, {}, 0, 0
        for i, value in enumerate(nums):
            if value not in first:
                '''
                记录 value首次出现的位置
                '''
                first[value] = i
            counter[value] = counter.get(value, 0) + 1
            if counter[value] > degree:
                degree = counter[value]
                ans = i - first[value] + 1
            elif counter[value] == degree:
                ans = min(ans, i - first[value] + 1)
        return ans
