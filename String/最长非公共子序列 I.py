# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 14:16
# @Author  : Yippee Song
# @Software: PyCharm
'''
521 Longest Uncommon Subsequence I

There are three cases  possible with string a and b:

Case I: a==b.
If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return -1.

Case II:
length(a)=length(b) but a !=b.
​Example: abc and abd. In this case we can consider any string i.e. abcabc or abdabd as a required subsequence, as out of these two strings one string will never be a subsequence of other string. Hence, return length(a)length(a) or length(b)length(b).

Case III:
 length(a)!=length(b)
 Example abcd and abc. In this case we can consider bigger string as a required subsequence because bigger string can't be a subsequence of smaller string. Hence, return max(length(a),length(b))max(length(a),length(b)).
'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a==b:
            return -1
        else:
            return max(len(a),len(b))