# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:16
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            pass
        i = 0
        j = len(s)-1
        while i<=j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1