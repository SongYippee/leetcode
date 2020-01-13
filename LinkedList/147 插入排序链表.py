# -*- coding: utf-8 -*-
# @Time    : 1/13/20 10:38 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
用插入排序算法，排序链表
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        curr = root.next = head

        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                tmp = curr.next
                curr.next = curr.next.next
                pre = root
                while pre.next.val <= tmp.val:
                    pre = pre.next
                tmp.next = pre.next
                pre.next = tmp
        return root.next
