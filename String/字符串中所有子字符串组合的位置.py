class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        """
        Input:
          s = "barfoothefoobarman",
          words = ["foo","bar"]
        Output: [0,9]
          Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
        The output order does not matter, returning [9,0] is fine too.
        """
        
        if not words: return []
        m, n, o, target = len(s), len(words), len(words[0]), []
        for i in range(m-n*o+1):
            word_target = words[:]
            for k in range(n):
                word = s[i+k*o : i+k*o+o]
                if word in word_target: word_target.remove(word)
                else: break
            if not word_target: target.append(i)
        return target
