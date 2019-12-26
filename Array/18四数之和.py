# -*- coding: utf-8 -*-
# @Time    : 12/24/19 3:06 PM
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return None
        nums.sort()
        ans = set()
        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                left = j + 1
                right = length - 1
                while left < right:
                    current = nums[i] + nums[j] + nums[left] + nums[right]
                    if current == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                    if current <= target:
                        left += 1
                        while (left < right and nums[left] == nums[left - 1]): left += 1
                    if current >= target:
                        right -= 1
                        while (left < right and nums[right] == nums[right + 1]): right -= 1
        return ans


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print Solution().fourSum(nums, target)
