# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 17:04
# @Author  : Yippee Song
# @Software: PyCharm
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        def findMin(strs):
            minstr = strs[0]
            for s in strs:
                if len(s) < len(minstr):
                    minstr = s
            return minstr

        minstr = findMin(strs)
        for i in range(len(minstr), 0, -1):
            longest = minstr[0:i]
            temp = True
            for s in strs:
                temp = temp and s.startswith(longest)
                if not temp:
                    break
            if temp:
                return longest
        else:
            return ""


if __name__ == '__main__':
    data = ["flower","flow","flight"]
    print data
    print Solution().longestCommonPrefix(data)