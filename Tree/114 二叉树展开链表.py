# -*- coding: utf-8 -*-
# @Time    : 10/28/20 4:31 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def makeList(node):
            if not node.left and not node.right:
                return (node, node)
            head = node
            tail = node
            left = node.left
            right = node.right
            if left:
                node.left = None
                x, y = makeList(left)
                head.right = x
                tail.right = x
                tail = y
            if right:
                m, n = makeList(right)
                tail.right = m
                tail = n

            return (head, tail)

        if not root:
            return
        root, _ = makeList(root)


if __name__ == '__main__':
    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(5)
    x.left.left = TreeNode(3)
    x.left.right = TreeNode(4)
    x.right.right = TreeNode(6)

    Solution().flatten(x)
