# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 21:33
# @Author  : Yippee Song
# @Software: PyCharm

'''
895 Maximum Frequency Stack
FreqStack 是一个类似栈的数据结构，它的 pop返回离栈顶最近的出现频率最大的元素。

'''

import collections


class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter() # 用来存储元素频率
        self.m = collections.defaultdict(list) # 用来索引，当前频率对应的元素有哪些
        self.maxf = 0 # 记录最大频率

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freq[x] += 1
        self.maxf = max(self.maxf, self.freq[x])
        self.m[self.freq[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.m[self.maxf].pop()
        self.freq[x] -= 1
        if not self.m[self.maxf]:
            self.maxf -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

'''
Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
'''