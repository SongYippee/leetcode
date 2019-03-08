# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 15:02
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = None
        while head:
            rev,rev.next,head = head,rev,head.next
        return rev