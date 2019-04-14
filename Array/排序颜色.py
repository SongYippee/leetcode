# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 18:12
# @Author  : Yippee Song
# @Software: PyCharm

'''
75 Sort Colors
用0，1，2分别代表 红色，白色，蓝色。将相同的颜色放在一起，并按照红白蓝顺序排序。
要求原地替换，最少的空间复杂度
'''


# 用三个变量记录红白蓝的个数，然后依次赋值
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        else:
            num_r = 0
            num_w = 0
            num_b = 0
            for num in nums:
                if num == 0:
                    num_r += 1
                elif num == 1:
                    num_w += 1
                else:
                    num_b += 1
            for i in range(num_r):
                # 标记红色
                nums[i] = 0
            for i in range(num_r, num_r + num_w):
                # 标记白色
                nums[i] = 1
            for i in range(num_r + num_w, len(nums)):
                # 标记蓝色
                nums[i] = 2
