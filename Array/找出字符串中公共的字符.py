# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:24
# @Author  : Yippee Song
# @Software: PyCharm


'''
input: a = ["bella", "label", "roller"]
首先构造字典，字典的值是每个字符在对应单词中出现的次数
{
	'b': [1, 1, 0],
	'e': [1, 1, 1],
	'l': [2, 2, 2],
	'a': [1, 1, 0],
	'r': [0, 0, 2],
	'o': [0, 0, 1]
}

最后构造的结果：从数组中抽取最小值，构造字符
'''
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        book = {}
        lenA = len(A)
        for index,word in enumerate(A):
            for c in word:
                if c not in book:
                    book[c] = [0 for i in range(lenA)]
                book[c][index] = book[c][index]+1
        ans = []
        for k,v in book.items():
            times = min(v)
            if times >0:
                while times>0:
                    ans.append(k)
                    times -=1
        return ans


if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    print Solution().commonChars(A)