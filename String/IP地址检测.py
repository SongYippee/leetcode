# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:53
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        def checkIpV4(IP):
            nums = IP.split('.')
            if len(nums) != 4:
                return "Neither"
            for x in nums:
                try:
                    num = int(x, 10)
                    if x[0] == '-' or x[0] == '+':
                        return 'Neither'
                    if x[0] == '0' and len(x) > 1:
                        return 'Neither'
                    if num < 0 or num > 255:
                        return 'Neither'
                except:
                    return "Neither"
            return "IPv4"

        def checkIpV6(IP):
            IP = IP.upper()
            items = IP.split(':')
            if len(items) != 8:
                return 'Neither'
            for each in items:
                if len(each) == 0 or len(each) > 4:
                    return "Neither"
                try:
                    num = int(each, 16)
                    if each[0] == '-' or each[0] == '+':
                        return 'Neither'
                except:
                    return 'Neither'
            return "IPv6"

        if '.' in IP:
            return checkIpV4(IP)
        else:
            return checkIpV6(IP)