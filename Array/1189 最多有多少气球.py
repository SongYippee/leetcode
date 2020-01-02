# -*- coding: utf-8 -*-
# @Time    : 12/31/19 11:03 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        countA = 0
        countB = 0
        countL = 0
        countO = 0
        countN = 0

        if not text:
            return 0
        for c in text:
            if c == 'b':
                countB += 1
            elif c == 'a':
                countA += 1
            elif c == 'l':
                countL += 1
            elif c == 'o':
                countO += 1
            elif c == 'n':
                countN += 1
        countL = countL / 2
        countO = countO / 2

        return min(countA, countB, countL, countO, countN)

