# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 17:37
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        lenN = len(nums)
        i = 0
        j = lenN-1
        while i<=j:
            mid = int((i+j)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                j = mid - 1
            else:
                i = mid+1
        else:
            return -1