# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:13
# @Author  : Yippee Song
# @Software: PyCharm
'''
840 Magic Squares in Grid
从 grid中检测一共有多少个3x3的子矩阵，使子矩阵都是魔法矩阵。魔法矩阵的定义是 横竖斜三个方向的和都相同，且都是1-9的不重复数字
'''


class Solution(object):
    def check(self, grid, startrow, endrow, startcolumn, endcolumn):
        def checkrow():
            result = -1
            for row in range(startrow, endrow):
                if result == -1:
                    result = sum(grid[row][startcolumn:endcolumn])
                else:
                    if result != sum(grid[row][startcolumn:endcolumn]):
                        return False
            return True

        def checkcolumn():
            result = -1
            for column in range(startcolumn, endcolumn):
                temp = 0
                for row in range(startrow, endrow):
                    temp += grid[row][column]
                if result == -1:
                    result = temp
                else:
                    if result != temp:
                        return False
            return True

        def checkdiagonals():
            first = 0
            second = 0
            row = startrow
            column = startcolumn
            while row < endrow and column < endcolumn:
                first += grid[row][column]
                row += 1
                column += 1

            row = startrow
            column = endcolumn - 1
            while row < endrow and column >= 0:
                second += grid[row][column]
                row += 1
                column -= 1
            return first == second

        def checkcontiguous():
            temp = set()
            for row in range(startrow, endrow):
                for column in range(startcolumn, endcolumn):
                    if grid[row][column] in xrange(1, 10):
                        temp.add(grid[row][column])
                    else:
                        return False
            return len(temp) == (endrow - startrow) * (endcolumn - startcolumn)

        return checkcontiguous() and checkrow() and checkcolumn() and checkdiagonals()

    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        if row < 3 or column < 3:
            return 0
        cnt = 0
        for r in range(row):
            endr = r + 3
            if endr > row:
                break
            for c in range(column):
                endc = c + 3
                if endc > column:
                    break
                if self.check(grid, r, endr, c, endc):
                    cnt += 1
        return cnt

