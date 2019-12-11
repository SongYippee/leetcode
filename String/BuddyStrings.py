# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 14:01
# @Author  : Yippee Song
# @Software: PyCharm
'''
859 Buddy Strings
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

示例 1：

输入： A = "ab", B = "ba"
输出： true
示例 2：

输入： A = "ab", B = "ab"
输出： false
示例 3:

输入： A = "aa", B = "aa"
输出： true
示例 4：

输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true
示例 5：

输入： A = "", B = "aa"
输出： false
 

提示：

0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。
'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A or not B or len(A) != len(B):
            return False
        differs = []
        for a_char, b_char in zip(A, B):
            if a_char != b_char:
                differs.append((a_char, b_char))
                if len(differs) > 2:
                    return False
        print differs
        if not differs and len(A) != len(set(A)):
            return True
        elif len(differs) == 1:
            return False
        elif len(differs) == 2 and (differs[0][0], differs[0][1]) == (differs[1][1], differs[1][0]):
            return True
        else:
            return False