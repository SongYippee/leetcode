# -*- coding: utf-8 -*-
# @Time    : 10/25/20 5:25 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        if not nums:
            return ans
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                i = mid
                while nums[i] == target:
                    i -= 1
                    if i < 0:
                        break
                ans[0] = (i + 1)
                j = mid
                while nums[j] == target:
                    j += 1
                    if j > right:
                        break
                ans[1] = (j - 1)
                return ans
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            return ans
