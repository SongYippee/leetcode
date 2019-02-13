# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:51
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str2num(str):
            l = len(str)
            if str == '0':
                return 0
            else:
                total = 0
                for i in range(l):
                    h = int(str[i])
                    total +=h*10**(l-i-1)
                return total
        return str(str2num(num1)*str2num(num2))

if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print num1+"*"+num2
    print Solution().multiply(num1,num2)