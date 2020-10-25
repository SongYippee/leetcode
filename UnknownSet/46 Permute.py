# -*- coding: utf-8 -*-
# @Time    : 10/25/20 6:38 PM
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = {}
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            def generate(arrays, newNumber):
                newArrays = []
                for each in arrays:
                    m = len(each)
                    for i in range(m + 1):
                        x = each[:]
                        x.insert(i, newNumber)
                        newArrays.append(x)
                return newArrays

            defaultArray = [[nums[0], nums[1]], [nums[1], nums[0]]]
            for i in range(2, n):
                defaultArray = generate(defaultArray, nums[i])
            return defaultArray


if __name__=="__main__":
    nums = [1,2,3,4]
    print Solution().permute(nums)