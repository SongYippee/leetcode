# -*- coding: utf-8 -*-
# @Time    : 12/24/19 2:30 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import math


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        threshold = math.floor(len(nums) / 3.0)
        temp = dict()
        ans = set()
        for n in nums:
            if n not in temp:
                temp[n] = 1
            else:
                temp[n] = temp[n] + 1
            if n not in ans and temp[n] > threshold:
                ans.add(n)
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print Solution().majorityElement(nums)
