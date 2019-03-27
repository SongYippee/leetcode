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
