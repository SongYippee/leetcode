class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        """
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        """
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l2.val < l1.val:
            l1, l2 = l2, l1
        head = l1
        while l1.next is not None:
            if l2 is None:
                return head
            if l2.val >= l1.val and l2.val <= l1.next.val:
                l1.next, l2.next, l2 = l2, l1.next, l2.next
            l1 = l1.next
        l1.next = l2
        return head
