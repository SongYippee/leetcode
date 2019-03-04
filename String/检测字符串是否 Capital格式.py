# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 13:43
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        length = len(word)
        temp = {'big': 0, 'small': 0}
        for c in word:
            if ord('A') <= ord(c) <= ord('Z'):
                temp['big'] += 1
            elif ord('a') <= ord(c) <= ord('z'):
                temp['small'] += 1

        if temp['big'] == length or temp['small'] == length:
            return True
        if ord('A') <= ord(word[0]) <= ord('Z') and temp['small'] == length - 1:
            return True
        return False