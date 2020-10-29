# -*- coding: utf-8 -*-
# @Time    : 10/29/20 2:36 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generate(rowIndex + 1)[-1]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        x = self.generate(numRows - 1)
        y = [1] * numRows
        for i in range(1, numRows - 1):
            y[i] = x[-1][i] + x[-1][i - 1]
        x.append(y)
        return x
