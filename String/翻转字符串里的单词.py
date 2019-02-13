# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:54
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个字符串，逐个翻转字符串中的每个单词。

示例:

输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        data = [x for x in s.split() if x]
        return " ".join(data[::-1])

if __name__ == '__main__':
    s = "the sky is blue"
    print Solution().reverseWords(s);