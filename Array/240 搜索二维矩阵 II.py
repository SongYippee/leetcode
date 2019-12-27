# -*- coding: utf-8 -*-
# @Time    : 12/26/19 3:49 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
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
        total_rows = len(matrix)
        if total_rows == 0:
            return False
        total_cols = len(matrix[0])
        if total_cols == 0:
            return False

        def search(M, row_start, row_end, col_start, col_end, target):
            print "search ( % d, % d, % d, % d) " % (row_start, row_end, col_start, col_end)
            if row_start >= total_rows or row_end >= total_rows or row_start > row_end or row_start < 0 or row_end < 0:
                print "row not match row_start=%d, row_end=%d" % (row_start, row_end)
                return False
            if col_start >= total_cols or col_end >= total_cols or col_start > col_end or col_start < 0 or col_end < 0:
                print "col not match col_start=%d, col_end=%d" % (col_start, col_end)
                return False
            if M[row_start][col_start] > target or target > M[row_end][col_end]:
                '''
                左上角元素大于目标值，或右下角元素小于目标值，则当前搜索范围内没有目标值，无需搜索
                '''
                return False
            mid_row = int((row_start + row_end) / 2)
            mid_col = int((col_start + col_end) / 2)
            print "M[%d][%d]=%d" % (mid_row, mid_col, M[mid_row][mid_col])
            if M[mid_row][mid_col] == target:
                return True
            elif M[mid_row][mid_col] < target:
                big_search = False
                print "so big, begin big search"
                print "first, begin big search at Down"
                big_search = search(M, mid_row + 1, row_end, mid_col, col_end, target)
                print "down_search=%s" % (str(big_search))
                if big_search:
                    return big_search
                else:
                    print "second, begin big search at Right"
                    big_search = search(M, mid_row, mid_row, mid_col + 1, col_end, target)
                    print "right_search=%s" % (str(big_search))
                    if big_search:
                        return big_search
                    else:
                        return search(M, row_start, mid_row - 1, mid_col + 1, col_end, target) \
                               or search(M, mid_row + 1, row_end, col_start, mid_col - 1, target)
            else:
                print "so small, begin small search"
                print "first, begin small search at Left"
                small = search(M, row_start, mid_row, col_start, mid_col - 1, target)
                print "left_search=%s" % str(small)
                if small:
                    return small
                else:
                    print "second, begin small search at UP"
                    small = search(M, row_start, mid_row - 1, mid_col, mid_col, target)
                    print "up_search=%s" % str(small)
                    if small:
                        return small
                    else:
                        return search(M, row_start, mid_row - 1, mid_col + 1, col_end, target) \
                               or search(M, mid_row + 1, row_end, col_start, mid_col - 1, target)

        return search(matrix, 0, total_rows - 1, 0, total_cols - 1, target)


class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        total_rows = len(matrix)
        if total_rows == 0:
            return False
        total_cols = len(matrix[0])
        if total_cols == 0:
            return False

        row, col = 0, total_cols - 1
        while row < total_rows and col >= 0:
            print "matrix[%d][%d]=%d" % (row, col, matrix[row][col])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 18
    print Solution2().searchMatrix(matrix, target)
