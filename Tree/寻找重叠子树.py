# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 11:16
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import Counter
from collections import defaultdict


def initTree(data):
    '''
    先序方式构造二叉树
    :param data:
    :return:
    '''
    if not data:
        return None
    head = TreeNode(data[0])
    currentLevel = [head]
    nextLevel = []
    i = 1
    while currentLevel and i < len(data):
        for node in currentLevel:
            if not node:
                continue
            else:
                if i < len(data) and data[i] != None:
                    node.left = TreeNode(data[i])
                i += 1
                if i >= len(data):
                    break
                if i < len(data) and data[i] != None:
                    node.right = TreeNode(data[i])
                i += 1
                if i >= len(data):
                    break
                nextLevel.append(node.left)
                nextLevel.append(node.right)
        else:
            currentLevel = nextLevel
            nextLevel = []
    return head


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = Counter()
        ans = []

        def makeId(node):
            if node:
                uid = trees[node.val, makeId(node.left), makeId(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        makeId(root)
        return ans


if __name__ == '__main__':
    '''
    Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
    '''
    data = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    binTree = initTree(data)
    print Solution().findDuplicateSubtrees(binTree)
