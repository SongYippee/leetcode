# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:48
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        book = {}
        for v in nums:
            if v not in book:
                book[v]=v
            else:
                return True
        else:
            return False