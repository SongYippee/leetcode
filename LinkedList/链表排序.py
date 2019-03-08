# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 16:42
# @Author  : Yippee Song
# @Software: PyCharm
'''
以 O(NlogN)的时间复杂度，实现链表排序，此处使用的是归并排序

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        '''
        通过 fase,slow将链表切分成两部分
        '''
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        '''
        second 代表后半部分的头结点
        '''
        second = slow.next
        '''
        slow.next=None表示前半部分到此结束
        '''
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, left, right):
        result_head = result_tail = None
        while left and right:
            if left.val < right.val:
                if not result_head:
                    result_head = left
                    result_tail = left
                else:
                    result_tail.next = left
                    result_tail = result_tail.next
                left = left.next
            else:
                if not result_head:
                    result_head = right
                    result_tail = right
                else:
                    result_tail.next = right
                    result_tail = result_tail.next
                right = right.next
        if left:
            if not result_head:
                result_head = left
            else:
                result_tail.next = left
        if right:
            if not result_head:
                result_head = right
            else:
                result_tail.next = right
        return result_head
