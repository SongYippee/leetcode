# -*- coding: utf-8 -*-
# @Time    : 12/31/19 10:36 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def __init__(self):
        self.my_dic = {}

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            self.my_dic[1] = ['()']
            return self.my_dic[1]
        else:
            if n not in self.my_dic:
                if n - 1 not in self.my_dic:
                    self.my_dic[n - 1] = self.generateParenthesis(n - 1)
                self.my_dic[n] = []
                preList = self.my_dic[n - 1]
                for each in preList:
                    indexs = [i for i, x in enumerate(each) if x == ')']
                    for i in indexs:
                        self.my_dic[n].append(each[:i] + "()" + each[i:])
                        self.my_dic[n].append(each[:i + 1] + "()" + each[i + 1:])
                self.my_dic[n] = list(set(self.my_dic[n]))

            return self.my_dic[n]


if __name__=='__main__':
    n=1
    print(Solution().generateParenthesis(n))