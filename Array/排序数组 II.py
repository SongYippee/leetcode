# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 17:08
# @Author  : Yippee Song
# @Software: PyCharm

'''
922 Sort Array By Parity II
偶数索引上的数字必须是偶数，奇数索引上的数必须是奇数
'''


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddIndex = 0
        evenIndex = 1
        while oddIndex < len(A) and evenIndex < len(A):
            if A[oddIndex] % 2 == 0:
                oddIndex += 2
            else:
                i = oddIndex + 1
                while i < len(A):
                    if A[i] % 2 == 0:
                        break
                    else:
                        i += 1
                if i < len(A):
                    A[oddIndex], A[i] = A[i], A[oddIndex]
                    oddIndex +=2
                else:
                    break
            if A[evenIndex] % 2 == 1:
                evenIndex += 2
            else:
                i = evenIndex + 1
                while i < len(A):
                    if A[i] % 2 == 1:
                        break
                    else:
                        i += 1
                if i < len(A):
                    A[evenIndex], A[i] = A[i], A[evenIndex]
                    evenIndex+=2
                else:
                    break
        return A

if __name__ == '__main__':
    A = [3,1,4,2]
    print Solution().sortArrayByParityII(A)