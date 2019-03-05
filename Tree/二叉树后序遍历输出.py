# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 17:06
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        if not root:
            return data
        if root.left:
            data.extend(self.postorderTraversal(root.left))
        if root.right:
            data.extend(self.postorderTraversal(root.right))
        data.append(root.val)
        return data