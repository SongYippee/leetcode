# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 14:01
# @Author  : Yippee Song
# @Software: PyCharm
'''
859 Buddy Strings
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