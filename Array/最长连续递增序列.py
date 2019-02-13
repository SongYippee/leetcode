# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 17:07
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
'''


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxl = []
        maxa = 0
        for c in nums:
            if not maxl or c > maxl[-1]:
                maxl.append(c)
            else:
                maxl = []
                maxl.append(c)
            maxa = max(maxa, len(maxl))
        return maxa


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    print Solution().findLengthOfLCIS(nums)
