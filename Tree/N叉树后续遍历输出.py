# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 17:03
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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        data = []
        if not root:
            return data
        if root.children:
            for child in root.children:
                if child:
                    data.extend(self.postorder(child))
        data.append(root.val)
        return data
