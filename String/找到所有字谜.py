# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 16:53
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        p = sorted(p)
        window = len(p)
        for i in range(len(s)-window+1):
            sub = s[i:i+window]
            if sorted(sub) == p:
                ans.append(i)
        return ans