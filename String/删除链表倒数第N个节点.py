class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        """
        Given linked list: 1->2->3->4->5, and n = 2.
        After removing the second node from the end, the linked list becomes 1->2->3->5.
        """
        
        length, count, dummy = 1, 1, head
        while dummy.next:
            length, dummy = length + 1, dummy.next
        if length == n:
            return head.next
        dummy = head
        while count < length - n:
            count, dummy = count + 1, dummy.next
        dummy.next = dummy.next.next
        return head
        
