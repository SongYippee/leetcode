# -*- coding: utf-8 -*-
# @Time    : 1/9/20 3:00 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not k or not head or not head.next:
            return head
        first = tmp = head
        N = 0
        while tmp:
            tmp = tmp.next
            N += 1
        if k % N == 0:
            return first
        i = N - k % N
        tmp = head
        pre = None
        while i > 0:
            tmp = tmp.next
            if not pre:
                pre = head
            else:
                pre = pre.next
            i -= 1

        second = tmp
        pre.next = None
        while tmp.next:
            tmp = tmp.next
        tmp.next = first
        return second
