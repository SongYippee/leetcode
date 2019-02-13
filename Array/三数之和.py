# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 17:02
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        ans = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if -(nums[i]+nums[j]) in dic and dic[-(nums[i]+nums[j])][-1] >j:
                    x = [nums[i],nums[j],-(nums[i]+nums[j])]
                    if x not in ans:
                        ans.append(x)
        return  ans

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(nums)