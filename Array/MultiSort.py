# -*- coding: utf-8 -*-
# @Time    : 10/26/20 4:33 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
多种排序算法实现
'''


class Solution(object):

    def merge_seq(self, left, right):
        ans = []
        n1 = len(left)
        n2 = len(right)
        i = 0;
        j = 0
        while (i < n1 and j < n2):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        if i < n1:
            ans.extend(left[i:])
        if j < n2:
            ans.extend(right[j:])
        return ans

    def mergeSort(self, nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) / 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge_seq(left, right)

    def fastSort(self, nums):

        def sort(nums, start, end):
            if start < end:
                base = nums[start]
                i = start
                j = end
                while i < j:
                    while i < j and nums[j] > base:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1
                    while i < j and nums[i] <= base:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1
                nums[i] = base
                sort(nums, start, i - 1)
                sort(nums, i + 1, end)

        sort(nums, 0, len(nums) - 1)
        return nums

    def maopaoSort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def insertSort(self, nums):
        ans = []
        n = len(nums)
        if n <= 1:
            return nums
        for i in range(n):
            if not ans:
                ans.append(nums[i])
            else:
                ansL = len(ans)
                j = 0
                if nums[i] <= ans[0]:
                    ans.insert(0, nums[i])
                elif nums[i] >= ans[-1]:
                    ans.append(nums[i])
                else:
                    while j < ansL and ans[j] < nums[i]:
                        j += 1
                    ans.insert(j,nums[i])

        return ans


if __name__ == "__main__":
    nums = [4, 2, 5, 7, 6,3]
    # print Solution().mergeSort(nums)
    # print Solution().fastSort(nums)
    # print Solution().maopaoSort(nums)
    print Solution().insertSort(nums)
