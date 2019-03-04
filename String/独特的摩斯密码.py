# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 16:03
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        book = dict(zip(alpha,code))
        print book
        if not words:
            return 0
        ans = set()
        for word in words:
            encode = ''
            for w in word:
                encode +=book[w]
            ans.add(encode)
        return len(ans)