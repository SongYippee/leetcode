# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:59
# @Author  : Yippee Song
# @Software: PyCharm
# TODO 优化，当前实现运行会超时

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        i = 0
        j = 1
        lenN = len(nums)
        while i < j and j < lenN:
            if abs(nums[i] - nums[j]) <= t and j - i <= k:
                return True
            else:
                if j - i <= k:
                    j += 1
                    if j == lenN and i<lenN:
                        '''某一趟 j走到头了，换一个 i，j 试试'''
                        i = i+1
                        j = i+1
                else:
                    i += 1
                    j = i+1
        return False

if __name__ == '__main__':
    nums = [7,1,3]
    k = 2
    t = 3
    print Solution().containsNearbyAlmostDuplicate(nums,k,t)