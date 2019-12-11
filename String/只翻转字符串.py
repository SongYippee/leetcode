# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 14:40
# @Author  : Yippee Song
# @Software: PyCharm

'''
917 仅仅翻转字符

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-only-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        i = 0
        j = len(S) - 1
        ans = ["" for _ in range(len(S))]
        while i <= j:
            if S[i].isalpha() and S[j].isalpha():
                ans[i], ans[j] = S[j], S[i]
                i += 1
                j -= 1
            elif not S[i].isalpha():
                ans[i] = S[i]
                i += 1
            elif not S[j].isalpha():
                ans[j] = S[j]
                j -= 1
        return ''.join(ans)
