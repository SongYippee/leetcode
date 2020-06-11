# -*- coding: utf-8 -*-
# @Time    : 1/14/20 10:17 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        first = None
        firstTmp = None
        second = None
        secondTmp = None

        tmp = head
        while tmp:
            nextNode = tmp.next
            if tmp.val < x:
                if not first:
                    first = tmp
                    firstTmp = first
                else:
                    firstTmp.next = tmp
                    firstTmp = firstTmp.next
                tmp.next = None
            else:
                if not second:
                    second = tmp
                    secondTmp = tmp
                else:
                    secondTmp.next = tmp
                    secondTmp = secondTmp.next
                tmp.next = None
            tmp = nextNode
        if firstTmp:
            firstTmp.next = second
            return first
        else:
            return second
