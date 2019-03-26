class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        """
        
        result = 0
        symbols = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        length = len(s)
        index = 0
        while index < length:
            last = index + 1
            while last < length:
                if s[index:last] in symbols:
                    last += 1
                else:
                    break
            if last == length:
                if s[index:last] in symbols: 
                    result += symbols[s[index:last]]
                    index = last
                else:
                    result += symbols[s[index:last-1]]
                    index = last-1
            else:
                result += symbols[s[index:last-1]]
                index = last-1
        return result
            
