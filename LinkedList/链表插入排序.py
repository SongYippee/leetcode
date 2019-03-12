# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 17:04
# @Author  : Yippee Song
# @Software: PyCharm

import copy
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

        #TODO 当前版本提交，运行会超时
        def insert(linked, node):
            if not linked:
                node.next = None
                return node
            head = temp = linked
            pre = None
            while temp:
                if temp.val < node.val:
                    pre, temp = temp, temp.next
                else:
                    if not pre:
                        head = node
                        head.next = temp
                        break
                    else:
                        node.next = temp
                        pre.next = node
                        break
            else:
                pre.next = node
                pre.next.next = None
            return head

        x = None
        while head:
            node = copy.deepcopy(head)
            node.next = None
            x = insert(x, node)
            head = head.next
        return x

if __name__ == '__main__':
    data = [4,2,1,3]
    def makeList(data):
        temp = head = ListNode(data[0])
        for i in range(1,len(data)):
            temp.next = ListNode(data[i])
            temp = temp.next
        return head
    head = makeList(data)
    Solution().insertionSortList(head)