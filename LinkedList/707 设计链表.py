# -*- coding: utf-8 -*-
# @Time    : 1/5/20 11:13 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        if self.length <= index:
            return -1
        if index == 0:
            return self.head.val
        elif index == self.length - 1:
            return self.tail.val
        else:
            step = 0
            tmp = self.head
            while tmp and step < index:
                tmp = tmp.next
                step += 1
            return tmp.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        tmp = ListNode(val)
        if self.length == 0:
            self.head = tmp
            self.tail = tmp
        else:
            tmp.next = self.head
            self.head = tmp
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        tmp = ListNode(val)
        if self.length == 0:
            self.head = tmp
            self.tail = tmp
        else:
            self.tail.next = tmp
            self.tail = tmp
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            node = ListNode(val)
            step = 0
            tmp = self.head
            while tmp and step < index - 1:
                tmp = tmp.next
                step += 1
            node.next = tmp.next
            tmp.next = node
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.length:
            return
        if self.length > 1:
            if index == 0:
                self.head = self.head.next
                self.length -= 1
                return
            else:
                step = 0
                tmp = self.head
                while tmp and step < index - 1:
                    tmp = tmp.next
                    step += 1
                tmp.next = tmp.next.next
                if index == self.length - 1:
                    self.tail = tmp
                self.length -= 1
                if self.length == 1:
                    self.head = tmp
                    self.tail = tmp
                return
        elif self.length == 1:
            self.length = 0
            self.head = None
            self.tail = None
            return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
