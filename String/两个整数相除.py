'''
29 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        """
        Example 1:
          Input: dividend = 10, divisor = 3
          Output: 3
          
        Example 2:
          Input: dividend = 7, divisor = -3
          Output: -2
        """        
        
        flag = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            sub = divisor
            count = 1
            while dividend >= sub + sub:
                sub = sub + sub
                count = count + count
            dividend -= sub
            result += count
        if flag:
            result = -result
        return min(result, 2**31 - 1)
