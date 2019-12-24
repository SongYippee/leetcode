# -*- coding: utf-8 -*-
# @Time    : 12/24/19 5:11 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                return self.binarySearch(matrix[i], 0, cols - 1, target)
            if target > matrix[i][-1]:
                continue

    def binarySearch(self, row, i, j, target):
        if i > j:
            return False
        mid = (i + j) / 2
        if row[mid] == target:
            return True
        else:
            if row[mid] < target:
                return self.binarySearch(row, mid + 1, j, target)
            else:
                return self.binarySearch(row, i, mid - 1, target)


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print Solution().searchMatrix(matrix, target)
