# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:58
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        length = len(s)
        ans = []
        for i in range(1, 4):
            if int(s[0:i]) > 255 or len(s[0:i]) > 1 and s[0:i].startswith("0"):
                continue
            for j in range(1, 4):
                if i + j >= length or int(s[i:i + j]) > 255 or len(s[i:i + j]) > 1 and s[i:i + j].startswith("0"):
                    continue
                for k in range(1, 4):
                    if i + j + k >= length or int(s[i + j:i + j + k]) > 255 or int(s[i + j + k:]) > 255 or len(
                            s[i + j:i + j + k]) > 1 and s[i + j:i + j + k].startswith("0") or len(
                            s[i + j + k:]) > 1 and s[i + j + k:].startswith("0"):
                        continue
                    ans.append(s[0:i] + "." + s[i:i + j] + "." + s[i + j:i + j + k] + "." + s[i + j + k:])
        return ans

if __name__ == '__main__':
    s = "25525511135"
    print Solution().restoreIpAddresses(s)