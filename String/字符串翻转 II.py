# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:11
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ""
        if k <= 0:
            return s
        lenN = len(s)
        if lenN < k:
            return s[-1::-1]
        ans = ""
        for i in range(0, lenN, 2 * k):
            ans += s[i:i + k][-1::-1]
            if i + 2 * k < lenN:
                ans += s[i + k:i + 2 * k]
            else:
                ans += s[i + k:]
        return ans

