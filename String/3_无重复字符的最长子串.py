# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 16:37
# @Author  : Yippee Song
# @Software: PyCharm

'''

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        print self.method1(s)
        print self.method2(s)
        print self.method3(s)

    def method1(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        sl = len(set(s))
        if sl <= 2 or l == sl:
            return sl
        else:
            for i in range(sl, 2, -1):
                for j in range(l - i + 1):
                    sub = s[j:j + i]
                    if len(set(sub)) == i:
                        return i

    def method2(self,s):
        start = end = 0
        ans = 0
        dic = {}
        while start <= end < len(s):
            if s[end] in dic:
                start = max(dic[s[end]] + 1, start)
            dic[s[end]] = end
            ans = max(ans, end - start + 1)
            end += 1
        return ans

    def method3(self,s):
        sub = ''
        ans = 0
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                dup = sub.find(char)
                sub = sub[dup + 1:] + char
        return ans


if __name__ == '__main__':
    data = "abcdabccc"
    Solution().lengthOfLongestSubstring(data)
