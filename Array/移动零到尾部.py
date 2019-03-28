# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 16:32
# @Author  : Yippee Song
# @Software: PyCharm

'''
283 Move Zeroes，要求原地替换，不能复制数组

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        startZero, zeroIndex = 0, 0
        while startZero < len(nums) and zeroIndex < len(nums):
            while startZero < len(nums) and nums[startZero] != 0:
                '''
                找出首个0的位置
                '''
                startZero += 1
            if startZero == len(nums):
                break
            zeroIndex = max(startZero, zeroIndex) #确定0的位置
            while zeroIndex < len(nums) and nums[zeroIndex] == 0:
                '''
                一直偏移，找到非0的位置
                '''
                zeroIndex += 1
            if zeroIndex == len(nums):
                break
            elif nums[startZero] == 0 and nums[zeroIndex] != 0:
                nums[startZero] = nums[zeroIndex]
                nums[zeroIndex] = 0






