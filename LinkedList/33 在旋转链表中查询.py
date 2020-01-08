# -*- coding: utf-8 -*-
# @Time    : 1/7/20 10:36 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)

        def binarySearch(start, end, data, target):
            if start > end or start >= N or end >= N:
                return -1
            mid = (start + end) / 2
            if data[mid] == target:
                return mid
            elif data[mid] > target:
                return binarySearch(start, mid - 1, data, target)
            else:
                return binarySearch(mid + 1, end, data, target)

        def combineSearch(start, end, data, target):
            if start > end or start >= N or end >= N:
                return -1
            mid = (start + end) / 2
            if data[mid] == target:
                return mid
            else:
                if data[mid] >= data[start]:
                    # left ok
                    if data[mid] > target and target >= data[start]:
                        return binarySearch(start, mid - 1, data, target)
                    else:
                        return combineSearch(mid + 1, end, data, target)
                if data[mid] <= data[end]:
                    # right ok
                    if target > data[mid] and target <= data[end]:
                        return binarySearch(mid + 1, end, data, target)
                    else:
                        return combineSearch(start, mid - 1, data, target)

        return combineSearch(0, N - 1, nums, target)