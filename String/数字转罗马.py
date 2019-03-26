class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        """
        Example:
            Input: 1994
            Output: "MCMXCIV"
            Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        """
        
        symbols = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        keys = sorted(symbols, reverse=True)
        result = {}
        result_key = []
        for item in keys:
            shang = num / item
            yushu = num % item
            num = yushu
            if shang > 0:
                result[item] = shang
                result_key.append(item)
        result_str = ""
        for item in result_key:
            result_str += result[item] * symbols[item]
        return result_str
