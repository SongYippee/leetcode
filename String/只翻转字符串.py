# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 14:40
# @Author  : Yippee Song
# @Software: PyCharm

'''
917 Reverse Only Letters
'''
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        i = 0
        j = len(S) - 1
        ans = ["" for _ in range(len(S))]
        while i <= j:
            if S[i].isalpha() and S[j].isalpha():
                ans[i], ans[j] = S[j], S[i]
                i += 1
                j -= 1
            elif not S[i].isalpha():
                ans[i] = S[i]
                i += 1
            elif not S[j].isalpha():
                ans[j] = S[j]
                j -= 1
        return ''.join(ans)
