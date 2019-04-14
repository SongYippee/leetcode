# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 18:40
# @Author  : Yippee Song
# @Software: PyCharm

'''
48 图像旋转90度
1 2 3     7 4 1
4 5 6 --->8 5 2
7 8 9     9 6 3

'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, column = len(matrix), len(matrix[0])

        i, j = 0, row - 1
        # 先上下交换行数据
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        # 沿对角线交换数据
        for i in range(row):
            for j in range(i + 1, column):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]