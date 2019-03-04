# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 13:13
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s == s[-1::-1]:
            return len(s)
        temp = {}
        for x in s:
            if x not in temp:
                temp[x] = 1
            else:
                temp[x] += 1

        longest = 0
        allJishu = 0
        allOushu = 0
        first = False
        for k, v in temp.items():
            if v % 2 == 1 and v > 1:
                if first == False:
                    '''第一个奇数无需减1'''
                    allJishu += v
                    first = True
                else:
                    '''其他奇数减1'''
                    allJishu += (v - 1)
            elif v % 2 == 0:
                allOushu += v
        longest = allOushu + allJishu
        return longest


if __name__ == '__main__':
    s = "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
    print Solution().longestPalindrome(s)
