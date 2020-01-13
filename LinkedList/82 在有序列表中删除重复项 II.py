# -*- coding: utf-8 -*-
# @Time    : 1/13/20 10:16 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        zero = ListNode(-1111111111)
        zero.next = head
        tail=zero
        end = zero
        tailPre = None
        while end:
            while end.next and end.val==end.next.val:
                tail = tailPre # 有重复项，重置 tail
                end = end.next
            tail.next = end.next
            tailPre = tail
            tail = tail.next
            end = end.next
        return zero.next