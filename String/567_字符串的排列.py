# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 17:13
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def allIsZero(x):
            for i in range(len(x)):
                if x[i] != 0:
                    return False
            return True

        if not s1 or not s2 or len(s1) > len(s2):
            return False
        cnt1 = [0 for i in range(26)]
        cnt2 = [0 for i in range(26)]
        for i in range(len(s1)):
            cnt1[ord(s1[i]) - 97] += 1
            cnt2[ord(s2[i]) - 97] += 1
        diff = [0 for i in range(26)]
        for i in range(26):
            diff[i] = cnt2[i] - cnt1[i]

        for i in range(len(s1), len(s2)):
            if allIsZero(diff):
                return True
            diff[ord(s2[i - len(s1)]) - 97] -= 1
            diff[ord(s2[i]) - 97] += 1
        return allIsZero(diff)

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print Solution().checkInclusion(s1,s2)