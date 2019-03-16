# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 21:32
# @Author  : Yippee Song
# @Software: PyCharm
'''
944 Delete Columns to Make Sorted
'''

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        def judge(cs):
            return sorted(cs) == cs
        if len(A[0]) == 1:
            return 0
        cnt = 0
        for i in range(len(A[0])):
            x = [A[j][i] for j in range(len(A))]
            if not judge(x):
                cnt+=1
        return cnt