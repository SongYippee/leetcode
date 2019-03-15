# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 16:45
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre=-float('inf')
        self.ans=float('inf')
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.getMinimumDifference(root.left)
        self.ans = min(self.ans, abs(root.val - self.pre))
        self.pre = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.ans