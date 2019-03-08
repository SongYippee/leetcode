# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 14:55
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first_half = None
        fast_index = head
        second_half = head
        while fast_index and fast_index.next:
            '''
            fast_index速度比 second_half快一倍，所以 fast_index到尾部的时候，second_half刚好在链表中间
            '''
            fast_index = fast_index.next.next
            first_half,first_half.next,second_half = second_half,first_half,second_half.next
        if fast_index:
            second_half = second_half.next
        while first_half and first_half.val == second_half.val:
            first_half = first_half.next
            second_half = second_half.next
        return not first_half