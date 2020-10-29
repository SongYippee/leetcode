# -*- coding: utf-8 -*-
# @Time    : 10/28/20 11:15 AM
# @Author  : Yippee Song
# @Software: PyCharm
'''

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        if len(nums)>=2:
            mid = (len(nums)-1)/2
            x = TreeNode(nums[mid])
            x.left = self.sortedArrayToBST(nums[:mid])
            x.right = self.sortedArrayToBST(nums[mid+1:])
            return x


if __name__=="__main__":
    nums=[-10,-3,0,5,9]
    head =Solution().sortedArrayToBST(nums)
    print head.val
    print head.left.val
    print head.right.val