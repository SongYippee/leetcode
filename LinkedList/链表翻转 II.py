# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 15:40
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        need_reverse = None # 保存需要翻转的部分
        reverse_head = reverse_tail = None
        pre = None # 保存需要连接翻转部分的那个节点
        i = 1
        index = head
        while index:
            if m<=i<=n:
                if i==m: # 翻转部分的尾节点
                    reverse_tail = index
                need_reverse,need_reverse.next,index = index,need_reverse,index.next
                if i==n:
                    reverse_head = need_reverse # 翻转部分的头节点
                i+=1
                if not index:# 翻转部分在链表的尾部，且已经是最后一个节点了，需要和前面不翻转的部分连接
                    if pre:
                        pre.next = reverse_head
                    else:
                        head = reverse_head
                    reverse_tail.next = index
            else:
                if i<m:
                    pre,index = index,index.next
                    i+=1
                if i>n:
                    if pre:
                        pre.next = reverse_head
                    else:
                        head = reverse_head
                    reverse_tail.next = index
                    break
        return head