# -*- coding: utf-8 -*-
# @Time    : 10/28/20 2:05 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)
        if lh > 0 and rh > 0:
            return min(lh, rh) + 1
        if lh > 0:
            return lh + 1
        else:
            return rh + 1
