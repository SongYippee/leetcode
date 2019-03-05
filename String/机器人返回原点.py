# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 17:24
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True
        else:
            if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
                return True
            return False