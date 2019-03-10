# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 11:23
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        words = S.split(' ')
        vowels = {'a','A','e',"E",'i','I','o','O','u','U'}
        for i,word in enumerate(words):
            if word[0] in vowels:
                words[i] = words[i]+'ma'+'a'*(i+1)
            else:
                words[i] = words[i][1:]+words[i][0]+'ma'+'a'*(i+1)
        return ' '.join(words)