# -*- coding: utf-8 -*-
# @Time    : 10/28/20 5:17 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个**完美**二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

         1                              1--->NULL
       /   \                         /--->\
      2     3                       2 ---->3-->NULL
    /  \  /  \                   /    \   /  \
  4    5  6  7                  4 --> 5-->6-->7-->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        下一层，依赖上一层已经完成next链接
        pre     指向上一层第一个节点
        parent  指向当前节点的父节点
        cur     指向当前节点
        """
        if not root:
            return root

        pre = root
        cur = root.left
        parent = root
        while pre:
            while cur:
                if parent.right != cur:
                    cur.next = parent.right
                    cur = cur.next
                else:
                    if parent.next:
                        cur.next = parent.next.left
                        cur = cur.next
                        parent = parent.next
                    else:
                        cur = None
            parent = pre.left
            pre = pre.left
            if parent:
                cur = parent.left
        return root
