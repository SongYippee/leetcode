# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 10:37
# @Author  : Yippee Song
# @Software: PyCharm

'''
832 Flipping an Image
'''


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return []
        for i, row in enumerate(A):
            temp = []
            for j in row[-1::-1]:
                if j == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            A[i] = temp
        return A
