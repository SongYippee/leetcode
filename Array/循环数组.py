# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 22:55
# @Author  : Yippee Song
# @Software: PyCharm

'''
457 Circular Array Loop
判断数组中是否有一个环，即数组下标 i 的轨迹是一个环。
0->3->2->0
nums[i]=k
如果 k>0，即前进 k 步，i+k
如果 k<0，即后退 k 步，i+k
'''


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False
        indexes = []
        n = len(nums)

        def nextIndexDirect(i):
            res = None
            res = i + nums[i]
            if res >= n:
                res = res % n
            if res < 0:
                res = res % n
            if nums[res] > 0:
                direct = 1
            else:
                direct = -1
            return res, direct

        indexes.append(0)
        direction = 1 if nums[0] > 0 else -1
        nxIndex, direct = nextIndexDirect(0)
        while nxIndex not in indexes and direction == direct:
            indexes.append(nxIndex)
            nxIndex, direct = nextIndexDirect(nxIndex)
        if nxIndex in indexes:
            i = indexes.index(nxIndex)
            if len(indexes) - i > 1:
                temp =indexes[i:]
                temp.append(nxIndex)
                print '-->'.join(map(str,temp))
                return True
            return False
        else:
            return False

if __name__ == '__main__':
    nums = [2,-1,1,2,2]
    print Solution().circularArrayLoop(nums)



