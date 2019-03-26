class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        """
        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        """      
        
        data_info = {"2":["a", "b", "c"], 
                    "3":["d", "e", "f"],
                    "4":["g", "h", "i"], 
                    "5":["j", "k", "l"], 
                    "6":["m", "n", "o"], 
                    "7":["p", "q", "r", "s"], 
                    "8":["t", "u", "v"], 
                    "9":["w", "x", "y", "z"]}
        result = []
        for item in digits:
            if result == []:
                result = data_info[item]
            else:
                cur_result = []
                for num in result:
                    for info in data_info[item]:
                        cur_result.append(num+info)
                result = cur_result
        return result
