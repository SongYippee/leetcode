# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:00
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        temp = s.split(' ')
        ans = []
        for x in temp:
            ans.append(x[-1::-1])
        return ' '.join(ans)