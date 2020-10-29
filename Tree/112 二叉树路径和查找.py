# -*- coding: utf-8 -*-
# @Time    : 10/28/20 2:55 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack=[]
        stack.append((root,root.val))

        while stack:
            node,path = stack.pop()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                stack.append((node.left,path+node.left.val))
            if node.right:
                stack.append((node.right,path+node.right.val))
        return False


if __name__ == "__main__":
    x = TreeNode(5)
    x.left = TreeNode(4)
    x.right = TreeNode(8)
    x.left.left = TreeNode(11)
    x.left.left.left = TreeNode(7)
    x.left.left.right = TreeNode(2)

    x.right.left = TreeNode(13)
    x.right.right = TreeNode(4)
    x.right.right.right = TreeNode(1)


    print Solution().hasPathSum(x, 22)
