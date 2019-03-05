# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 16:19
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        data = []
        if not root:
            return data
        if root.left:
            data.extend(self.inorderTraversal(root.left))
        data.append(root.val)
        if root.right:
            data.extend(self.inorderTraversal(root.right))
        return data