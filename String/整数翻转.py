# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 17:28
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31 or x < -2**31:
            return 0
        else:
            if abs(x)<=9:
                return x
            else:
                sign = 1 if x>0 else -1
                x = abs(x)
                h = x % 10
                r = x / 10
                after = h
                while r > 0:
                    h = r % 10
                    r = r / 10
                    after = after*10 +h
                if after*sign >= 2 ** 31 or after*sign < -2 ** 31:
                    return 0
                return after*sign


if __name__ == '__main__':
    print Solution().reverse(-123)