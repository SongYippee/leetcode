# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 16:36
# @Author  : Yippee Song
# @Software: PyCharm
'''
884 两句话中的非公共词
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。

 

示例 1：

输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：A = "apple apple", B = "banana"
输出：["banana"]
 

提示：

0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/uncommon-words-from-two-sentences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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