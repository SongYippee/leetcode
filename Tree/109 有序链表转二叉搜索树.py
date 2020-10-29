# -*- coding: utf-8 -*-
# @Time    : 10/28/20 11:31 AM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        思路，先将链表转数组，然后参考 108
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        n = len(array)

        def buildTree(array, start, end):
            if start > end or start < 0 or end >= n:
                return None
            mid = (start + end) / 2
            x = TreeNode(array[mid])
            x.left = buildTree(array, start, mid - 1)
            x.right = buildTree(array, mid + 1, end)
            return x

        return buildTree(array, 0, n - 1)
