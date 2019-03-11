# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 10:36
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        ans = ""
        ans+=str(t.val)
        if t.left and not t.right:
            ans+="("+self.tree2str(t.left)+")"
        elif not t.left and t.right:
            ans+="()("+self.tree2str(t.right)+")"
        elif t.left and t.right:
            ans+="("+self.tree2str(t.left)+")("+self.tree2str(t.right)+")"
        return ans