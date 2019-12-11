# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:30
# @Author  : Yippee Song
# @Software: PyCharm
'''
345 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        if not s:
            return s
        i = 0
        j = len(s)-1
        ans = list(s)
        while i<=j:
            if ans[i] not in vowels:
                i+=1
            elif ans[j] not in vowels:
                j-=1
            else:
                ans[i],ans[j] = ans[j],ans[i]
                i+=1
                j-=1
        return ''.join(ans)