# -*- coding: utf-8 -*-
# @Time    : 11/10/20 8:21 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def createNum(l):
            '''
            链表转数字
            :param l:
            :return:
            '''
            num = 0
            while l:
                num = 10 * num + l.val
                l = l.next
            return num

        num1 = createNum(l1)
        num2 = createNum(l2)
        sum = num1 + num2

        # 数字转链表
        n = len(str(sum))
        head = tail = ListNode(-1)
        while n > 0:
            base = 10 ** (n - 1)
            div = sum / base
            mod = sum % base
            tail.next = ListNode(div)
            tail = tail.next
            sum = mod
            n = n - 1
        return head.next
