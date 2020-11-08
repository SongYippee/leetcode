# -*- coding: utf-8 -*-
# @Time    : 11/8/20 5:12 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
两个链表代表两个数，实现两数之和
1->2->3,  4->5  代表数字 321 和 54

5->7->3，输出 375

'''


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def add(self, A, B):
        if not A:
            return B
        if not B:
            return A

        jinwei = 0
        head = tail = ListNode(-1)
        while (A and B):
            sum = A.val + B.val + jinwei
            jinwei = sum / 10
            remain = sum % 10
            tail.next = ListNode(remain)
            tail = tail.next
            A = A.next
            B = B.next

        x = A if A else B
        while (x):
            sum = x.val + jinwei
            jinwei = sum / 10
            remain = sum % 10
            tail.next = ListNode(remain)
            tail = tail.next
            x = x.next
        if jinwei > 0:
            tail.next = ListNode(jinwei)
        return head.next


if __name__ == '__main__':
    def makeList(x):
        head = tail = None
        for i, c in enumerate(x):
            if i == 0:
                head = tail = ListNode(c)
            else:
                tail.next = ListNode(c)
                tail = tail.next
        return head

    def getNum(x):
        ans = []
        while x:
            ans.append(x.val)
            x = x.next
        ans = ans[::-1]
        total=0
        for c in ans:
            total=(total*10+c)
        return total


    a = [1, 3, 4, 5,9]
    b = [2, 3, 6, 7,8]
    A = makeList(a)
    B = makeList(b)
    C = Solution().add(A, B)
    print "%d + %d = %d"%(getNum(A),getNum(B),getNum(C))
