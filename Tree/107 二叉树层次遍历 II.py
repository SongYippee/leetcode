# -*- coding: utf-8 -*-
# @Time    : 10/28/20 10:32 AM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            nextLevelNodes = [root]
            tmp = []
            levelVal = []
            while len(nextLevelNodes) > 0:
                node = nextLevelNodes.pop(0)
                levelVal.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                if len(nextLevelNodes) == 0:
                    nextLevelNodes = tmp
                    ans.append(levelVal)
                    levelVal = []
                    tmp = []
        return ans[-1::-1]


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

if __name__=="__main__":
    nums=[3,9,20,15,7]
    head=initTree(nums)
    print Solution().levelOrderBottom(head)
