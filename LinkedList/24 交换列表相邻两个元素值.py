'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Given 1->2->3->4, you should return the list as 2->1->4->3.
        """

        x = pre = ListNode(0)
        pre.next = head
        while pre and pre.next:
            left = pre.next
            right = left.next
            if not right:
                break
            left.next = right.next
            right.next = left
            pre.next = right
            pre = left
        return x.next
