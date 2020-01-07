# -*- coding: utf-8 -*-
# @Time    : 1/4/20 10:31 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        x = pre = ListNode(0)
        pre.next = head
        tmpHead = head

        def getTmpTail(node):
            step = 1
            while node and step < k:
                node = node.next
                step += 1
            if not node:
                return False
            else:
                return node

        def reverseList(node):
            X = ListNode(0)
            step = 0
            while node and node.next and step < k:
                nextNode = node.next
                node.next = X.next
                X.next = node
                node = nextNode
                step += 1
            if step == k:
                return X.next
            if not node.next:
                node.next = X.next
                X.next = node
                if step == k - 1:
                    return X.next
                else:
                    return reverseList(X.next)

        tmpTail = getTmpTail(tmpHead)
        while tmpTail:
            nextHead = tmpTail.next
            pre.next = reverseList(tmpHead)
            pre = tmpHead
            tmpHead = nextHead
            tmpTail = getTmpTail(nextHead)
            if not tmpTail:
                pre.next = nextHead
        return x.next


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
            txt += str(listData.val) + " "
            listData = listData.next
        print txt


    nums = [1, 2, 3, 4, 5]
    head = makeList(nums)
    printList(Solution().reverseKGroup(head, 2))
