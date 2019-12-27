# -*- coding: utf-8 -*-
# @Time    : 12/27/19 3:57 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        vNode = ListNode(0)
        vNode.next = head
        listLen = 0
        temp = head
        while temp:
            listLen += 1
            temp = temp.next

        preNodes = listLen - n

        temp = vNode
        while preNodes:
            preNodes -= 1
            temp = temp.next

        temp.next = temp.next.next
        return vNode.next


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
            txt+=str(listData.val)+" "
            listData = listData.next
        print txt

    nums = [1,2,3,4,5]
    head = makeList(nums)
    printList(Solution().removeNthFromEnd(head,1))
