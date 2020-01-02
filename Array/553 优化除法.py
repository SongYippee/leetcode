# -*- coding: utf-8 -*-
# @Time    : 1/1/20 10:05 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。

但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。

示例：

输入: [1000,100,10,2]
输出: "1000/(100/10/2)"
解释:
1000/(100/10/2) = 1000/((100/10)/2) = 200
但是，以下加粗的括号 "1000/((100/10)/2)" 是冗余的，
因为他们并不影响操作的优先级，所以你需要返回 "1000/(100/10/2)"。

其他用例:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
让分子最大，让分母变小
'''

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        N = len(nums)
        if N == 1:
            return str(nums[0])
        elif N == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            ans = [str(nums[0]), "/(", str(nums[1]), "/", str(nums[2])]
            i = 3
            while i < N:
                ans.append("/" + str(nums[i]))
                i += 1
            ans.append(")")
            return "".join(ans)


if __name__ == "__main__":
    nums = [1000, 100, 10, 2]
    print Solution().optimalDivision(nums)
