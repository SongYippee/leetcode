# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 13:56
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ""
        if K > 1:
            return ''.join(sorted(list(S)))
        if K == 1:
            if len(S) == 1:
                return S
            else:
                temp = S
                for i in range(1,len(S)):
                    if S[i:]+S[0:i] < temp:
                        temp = S[i:]+S[0:i]
                return temp


if __name__ == '__main__':
    S = 'kuh'
    print Solution().orderlyQueue(S, 1)
