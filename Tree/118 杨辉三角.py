# -*- coding: utf-8 -*-
# @Time    : 10/29/20 2:30 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
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
