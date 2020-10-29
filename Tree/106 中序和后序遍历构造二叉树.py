# -*- coding: utf-8 -*-
# @Time    : 10/29/20 2:20 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(inorder[0])
        head = TreeNode(postorder[-1])
        index_in_inorder = inorder.index(postorder[-1])
        inorder_left = inorder[:index_in_inorder]
        inorder_right = inorder[index_in_inorder + 1:]
        if inorder_left and not inorder_right:
            head.left = self.buildTree(inorder_left, postorder[:-1])
            head.right = None
        elif inorder_right and not inorder_left:
            head.right = self.buildTree(inorder_right, postorder[:-1])
            head.left = None
        else:
            head.left = self.buildTree(inorder_left, postorder[0:len(inorder_left)])
            head.right = self.buildTree(inorder_right, postorder[len(inorder_left):-1])
        return head
