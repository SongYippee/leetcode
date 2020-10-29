# -*- coding: utf-8 -*-
# @Time    : 10/28/20 1:48 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。


链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0
            left_hight = check(node.left)
            right_hight = check(node.right)
            if left_hight == -1 or right_hight == -1 or abs(left_hight - right_hight) > 1:
                return -1
            else:
                return max(left_hight, right_hight) + 1

        return check(root) >= 0
