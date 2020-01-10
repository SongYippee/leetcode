# -*- coding: utf-8 -*-
# @Time    : 1/10/20 11:10 AM
# @Author  : Yippee Song
# @Software: PyCharm

'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        tmp = head
        index = 0
        odd = otmp = ListNode(-1)
        even = etmp = ListNode(-2)
        while tmp:
            nextNode = tmp.next
            if index % 2 == 0:
                otmp.next = tmp
                otmp = otmp.next
                otmp.next = None
            else:
                etmp.next = tmp
                etmp = etmp.next
                etmp.next = None
            index += 1
            tmp = nextNode
        otmp.next = even.next
        return odd.next

if __name__=='__main__':
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
                txt += "->"
            listData = listData.next
        if not txt:
            txt = None
        print txt


    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    head = makeList(nums)
    printList(Solution().oddEvenList(head))
