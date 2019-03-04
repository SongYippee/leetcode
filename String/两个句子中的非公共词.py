# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 16:36
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]

        """

        book = {}
        listA = A.split(' ')
        listB = B.split(' ')
        for word in listA:
            if word not in book:
                book[word] = 1
            else:
                book[word] += 1
        for word in listB:
            if word not in book:
                book[word] = 1
            else:
                book[word] += 1
        ans = []
        for k, v in book.items():
            if v == 1:
                ans.append(k)
        return ans