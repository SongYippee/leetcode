# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 09:43
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):

    def check(self, s):
        notebook = {'max': ""}

        def process(s, i, j):
            if (i, j) not in notebook:
                if s[i:j] == s[i:j][-1::-1]:
                    notebook[(i, j)] = True
                    if len(s[i:j]) > len(notebook['max']):
                        notebook['max'] = s[i:j]
                else:
                    notebook[(i, j)] = False
                    if j - i < len(notebook['max']):
                        return
                    process(s, i, j - 1)
                    process(s, i + 1, j)
            else:
                return

        process(s, 0, len(s))
        return notebook['max']


if __name__ == '__main__':
    # TODO 长字符串提交会超时
    print Solution().check("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew")
