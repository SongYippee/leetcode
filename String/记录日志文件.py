# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 14:07
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []
        letter_logs = []
        digit_logs = []
        for x in logs:
            if x.split(' ')[1].isalpha():
                letter_logs.append(x)
            else:
                digit_logs.append(x)

        letter_logs.sort(key=lambda x: x.split(' ')[1:])
        letter_logs.extend(digit_logs)
        return letter_logs