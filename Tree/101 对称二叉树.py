# -*- coding: utf-8 -*-
# @Time    : 10/27/20 5:40 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''

给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        双指针检测
        """

        def check(ln, rn):
            if not ln and not rn:
                return True
            if not ln or not rn:
                return False
            else:
                return ln.val == rn.val and check(ln.left, rn.right) and check(ln.right, rn.left)

        return check(root, root)
