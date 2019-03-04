# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 14:42
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def findReplaceString(self, S, indices, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        modified = list(S)
        for index, source, target in zip(indices, sources, targets):
            if not S[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index + 1, index + len(source)):
                    modified[i] = ""

        return "".join(modified)


if __name__ == '__main__':
    S = "abcd";
    indexes = [0, 2];
    sources = ["a", "cd"];
    targets = ["eee", "ffff"]
    print Solution().findReplaceString(S, indexes, sources, targets)
