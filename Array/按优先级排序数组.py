# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 09:52
# @Author  : Yippee Song
# @Software: PyCharm
'''
将偶数放前面，奇数放后面
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while i < j:
            while i < len(A) and A[i] % 2 == 0:
                i += 1
            while j >= 0 and A[j] % 2 == 1:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        return A


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    print Solution().sortArrayByParity(A)
