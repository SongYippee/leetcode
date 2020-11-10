# -*- coding: utf-8 -*-
# @Time    : 11/10/20 8:24 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei = 0
        tail = head = ListNode(-1)
        while l1 and l2:
            sum = l1.val + l2.val + jinwei
            jinwei = sum / 10
            remain = sum % 10
            tail.next = ListNode(remain)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        x = l1 if l1 else l2
        if x:
            while x:
                sum = x.val + jinwei
                jinwei = sum / 10
                remain = sum % 10
                tail.next = ListNode(remain)
                tail = tail.next
                x = x.next
        if jinwei > 0:
            tail.next = ListNode(jinwei)
        return head.next
