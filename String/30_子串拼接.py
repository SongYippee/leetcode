# -*- coding: utf-8 -*-
# @Time    : 6/11/20 5:06 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.



Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

'''

import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        eachLen = len(words[0])
        totalWords = len(words)
        sLen = len(s)
        if sLen < totalWords * eachLen:
            return []

        wordsCount = {}
        for word in words:
            last = 0
            if (word in wordsCount):
                last = wordsCount[word]
                last += 1
            else:
                last = 1
            wordsCount[word] = last

        def isMatch(subStr, words):
            count = copy.deepcopy(wordsCount)
            for i in range(0, len(subStr), eachLen):
                word = subStr[i:i + eachLen]
                if word in count:
                    count[word] -= 1
                    if count[word] == 0:
                        count.pop(word)
                else:
                    return False
            if not count:
                return True

        result = []
        for i in range(0, sLen):
            subStr = s[i:i + totalWords * eachLen]
            if isMatch(subStr, words):
                result.append(i)
        return result


if __name__ == "__main__":
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    print Solution().findSubstring(s, words)
