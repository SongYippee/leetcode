# -*- coding: utf-8 -*-
# @Time    : 10/27/20 6:03 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nextLevelNodes = []
        ans = []

        if root:
            ans.append([root.val])
            if root.left:
                nextLevelNodes.append(root.left)
            if root.right:
                nextLevelNodes.append(root.right)

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
                    ans.append(levelVal)
                    nextLevelNodes = tmp
                    tmp = []
                    levelVal = []

        return ans
