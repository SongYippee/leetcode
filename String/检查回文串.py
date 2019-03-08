# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 14:19
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i,j = 0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].upper()!=s[j].upper():
                return False
            else:
                i+=1
                j-=1
        else:
            return True