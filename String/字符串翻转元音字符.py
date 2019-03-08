# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:30
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        if not s:
            return s
        i = 0
        j = len(s)-1
        ans = list(s)
        while i<=j:
            if ans[i] not in vowels:
                i+=1
            elif ans[j] not in vowels:
                j-=1
            else:
                ans[i],ans[j] = ans[j],ans[i]
                i+=1
                j-=1
        return ''.join(ans)