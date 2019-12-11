# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:00
# @Author  : Yippee Song
# @Software: PyCharm
'''
557 反转字符串中的单词
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        temp = s.split(' ')
        ans = []
        for x in temp:
            ans.append(x[-1::-1])
        return ' '.join(ans)