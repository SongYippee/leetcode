# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 16:59
# @Author  : Yippee Song
# @Software: PyCharm

'''
938 Range Sum of BST
给定 BST的根节点和 L,R两个值，返回 BST中节点值在范围[L,R]的和

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if not L<=R:
            return 0
        else:
            if root.val<L:
                # 从右子树中查找
                return self.rangeSumBST(root.right,L,R)
            elif root.val>R:
                # 从左子树中查找
                return self.rangeSumBST(root.left,L,R)
            else:
                # 拆分，从左右子树中查找
                return self.rangeSumBST(root.left,L,root.val-1)+root.val+self.rangeSumBST(root.right,root.val+1,R)