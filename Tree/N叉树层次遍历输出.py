# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 16:50
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def levelOrder(self,root):
        willTravelNodes = [root]
        result = []
        if not root:
            return result
        while willTravelNodes:
            nodesval = []
            for node in willTravelNodes:
                if node:
                    nodesval.append(node.val)
            result.append(nodesval)

            children = []
            for node in willTravelNodes:
                if node:
                    for child in node.children:
                        if child:
                            children.append(child)
            willTravelNodes = children
        return result