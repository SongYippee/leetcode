# -*- coding: utf-8 -*-
# @Time    : 1/9/20 10:04 AM
# @Author  : Yippee Song
# @Software: PyCharm

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        zero = ListNode(0)
        zero.next = head
        slow, fast = zero, zero
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if not fast.next or not fast.next.next:
                break
        second = slow.next
        slow.next = None

        def reverseList(node):
            tmp = ListNode(-1)
            while node:
                x = node
                node = node.next
                x.next = tmp.next
                tmp.next = x
            return tmp.next

        second = reverseList(second)
        first = zero.next
        tail = None
        while first:
            next_first = first.next
            next_second = second.next
            second.next = first.next
            first.next = second
            tail = second
            first = next_first
            second = next_second
        if second:
            tail.next = second
        return zero.next

if __name__ == '__main__':
    def makeList(data):
        head = ListNode(data[0])
        position = head
        for i in range(1, len(data)):
            temp = ListNode(data[i])
            position.next = temp
            position = temp
        return head


    def printList(listData):
        if not listData:
            print ""
        txt = ""
        while listData:
            txt += str(listData.val)
            if listData.next:
                txt+="->"
            listData = listData.next
        print txt


    nums = [1, 2, 3, 4,5,6]
    head = makeList(nums)
    reOrder = Solution().reorderList(head)
    printList(reOrder)
