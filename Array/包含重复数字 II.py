# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:37
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        book = {}
        for i, v in enumerate(nums):
            if v not in book:
                book[v] = i
            else:
                if i - book[v] <= k:
                    return True
                else:
                    book[v] = i
        else:
            return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print Solution().containsNearbyDuplicate(nums, k)
