# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 16:23
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        if not root:
            return data
        data.append(root.val)
        if root.left:
            data.extend(self.preorderTraversal(root.left))
        if root.right:
            data.extend(self.preorderTraversal(root.right))
        return data