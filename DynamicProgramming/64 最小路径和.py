# -*- coding: utf-8 -*-
# @Time    : 10/27/20 4:49 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid) #行数
        col = len(grid[0]) #列数

        dp = [[float('inf')] * col for _ in range(row)] # 初始化 dp的元素为无穷大
        dp[0][0] = grid[0][0]# 第一格的值等于 grid第一格的值

        # 初始化第一行 dp
        for i in range(1, col):
            dp[0][i] = grid[0][i] + dp[0][i - 1]

        # 初始化第一列 dp
        for i in range(1, row):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        # 计算其他 dp元素的值
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
