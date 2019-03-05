# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 16:28
# @Author  : Yippee Song
# @Software: PyCharm

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        data = []
        if not root:
            return data
        data.append(root.val)
        if root.children:
            for child in root.children:
                if child:
                    data.extend(self.preorder(child))
        return data
