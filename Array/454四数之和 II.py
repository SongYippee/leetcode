# -*- coding: utf-8 -*-
# @Time    : 12/26/19 3:08 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if len(A) == 0 or len(B) == 0 or len(C) == 0 or len(D) == 0:
            return 0
        lenN = len(A)

        def add(X, Y):
            ans = []
            for i in xrange(lenN):
                for j in xrange(lenN):
                    ans.append(X[i] + Y[j])
            return ans


        def indx(X):
            '''
            统计 X中每个元素的重复个数
            :param X:
            :return:
            '''
            ansDic = {}
            for i, num in enumerate(X):
                if num not in ansDic:
                    ansDic[num] = 1
                else:
                    ansDic[num] += 1
            return ansDic

        AB = add(A, B)
        CD = add(C, D)
        CDx = indx(CD)
        count = 0
        for x in AB:
            if -x in CDx:
                count += CDx[-x]
        return count


if __name__ == '__main__':
    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    print Solution().fourSumCount(A, B, C, D)
