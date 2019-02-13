# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 17:04
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
'''


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column = len(grid[0])
        row = len(grid)
        # print row,column
        visited = []
        for i in range(row):
            visited.append([])
            for j in range(column):
                visited[i].append(False)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        maxArea = 0

        def dfs(x, y, total):
            # print 'visit grid[%d][%d]=%d visited=%d'%(x,y,grid[x][y],visited[x][y])
            if grid[x][y] == 1 and visited[x][y] == False:
                total += 1
                visited[x][y] = True
                # print 'visit grid[%d][%d] set total=%d and visited[%d][%d]=True' % (x,y,total,x,y)
                for i in range(len(directions)):
                    currentDirection = directions[i]
                    nx = x + currentDirection[0]
                    ny = y + currentDirection[1]
                    if 0 <= nx < row and 0 <= ny < column and visited[nx][ny] == False:
                        # print 'next visit grid[%d][%d]' % (nx,ny)
                        total = dfs(nx, ny, total)
            return total

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 and visited[i][j] == False:
                    maxArea = max(dfs(i, j, 0), maxArea)
                    # print maxArea,i,j
        return maxArea


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print Solution().maxAreaOfIsland(grid)
