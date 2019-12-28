# -*- coding: utf-8 -*-
# @Time    : 12/28/19 11:07 PM
# @Author  : Yippee Song
# @Software: PyCharm

'''
在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
用这个程序你能收集的水果总量是多少？

示例 1：
输入：[1,2,1]
输出：3
解释：我们可以收集 [1,2,1]。

示例 2：
输入：[0,1,2,2]
输出：3
解释：我们可以收集 [1,2,2].
如果我们从第一棵树开始，我们将只能收集到 [0, 1]。

示例 3：
输入：[1,2,3,2,2]
输出：4
解释：我们可以收集 [2,3,2,2].
如果我们从第一棵树开始，我们将只能收集到 [1, 2]。

示例 4：
输入：[3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：我们可以收集 [1,2,1,1,2].
如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 个水果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fruit-into-baskets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree or len(tree) == 0:
            return 0
        N = len(tree)
        start, end = 0, 0
        temp = set()  # 存放水果类型，当类型大于 2 时，移除一个类型
        total_amount = 0
        while end < N:
            temp.add(tree[end])
            if (len(temp) > 2):
                if (end - start > total_amount):
                    total_amount = end - start
                '''
                将 temp 中的值，其在 tree中 index最小，将这个值移除
                '''
                if tree[end - 1] == tree[start]:
                    be_removed = end - 1
                    while tree[be_removed] == tree[start]:
                        be_removed -= 1
                    temp.remove(tree[be_removed])
                else:
                    temp.remove(tree[start])
                start = end - 1
                while tree[start - 1] == tree[start]:
                    start -= 1
            end += 1
        if end == N and end - start > total_amount:
            total_amount = end - start
        return total_amount


if __name__ == '__main__':
    tree = [4, 1, 1, 1, 3, 1, 7, 5]
    print Solution().totalFruit(tree)
