class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
        https://leetcode.com/problems/search-in-rotated-sorted-array/
        Your algorithm's runtime complexity must be in the order of O(log n).
        
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        """

        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            # mid之前是有序的
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # mid之后是有序的
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        
        
