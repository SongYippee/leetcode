# -*- coding: utf-8 -*-
# @Time    : 12/24/19 2:06 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
import math


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        temp = dict()
        threshold = math.floor(len(nums) / 2.0)
        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                temp[num] = temp[num] + 1
            if (temp[num] > threshold):
                return num


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print Solution().majorityElement(nums)
