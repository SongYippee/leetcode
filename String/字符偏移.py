# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 09:47
# @Author  : Yippee Song
# @Software: PyCharm

'''
848 Shifting Letters
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