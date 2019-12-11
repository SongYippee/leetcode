# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 09:47
# @Author  : Yippee Song
# @Software: PyCharm

'''
848 Shifting Letters

有一个由小写字母组成的字符串 S，和一个整数数组 shifts。

我们将字母表中的下一个字母称为原字母的 移位（由于字母表是环绕的， 'z' 将会变成 'a'）。

例如·，shift('a') = 'b'， shift('t') = 'u',， 以及 shift('z') = 'a'。

对于每个 shifts[i] = x ， 我们会将 S 中的前 i+1 个字母移位 x 次。

返回将所有这些移位都应用到 S 后最终得到的字符串。

示例：

输入：S = "abc", shifts = [3,5,9]
输出："rpl"
解释：
我们以 "abc" 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。
再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shifting-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        if not S:
            return ""
        if not shifts:
            return S
        def getshift(shifts,start):
            totalshift = reduce(lambda x,y:x+y,shifts[start:])
            return totalshift
        ans = ['' for _ in range(len(S))]
        for i in range(len(S)):
            if 97<=ord(S[i])<=122:
                ans[i]=chr((ord(S[i])+(getshift(shifts,i)%26))%122+97)
                if (ord(S[i])+(getshift(shifts,i)%26)) > 122:
                    ans[i] = chr((ord(S[i]) + (getshift(shifts, i) % 26)) % 122 + 97)
                else:
                    ans[i] = chr((ord(S[i]) + (getshift(shifts, i) % 26)))
            else:
                ans[i]=S[i]
        return ''.join(ans)

if __name__ == '__main__':
    S = 'ruu'
    shifts = [26,9,17]
    print Solution().shiftingLetters(S,shifts)