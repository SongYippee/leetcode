# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 16:09
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    '''
    逆中序遍历，pre记录上一次的值读取的节点值
    '''
    def __init__(self):
        self.pre = -float('inf')
        self.ans = float('inf')

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)
        self.ans = min(self.ans, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.ans

