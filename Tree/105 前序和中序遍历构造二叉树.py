# -*- coding: utf-8 -*-
# @Time    : 10/29/20 1:57 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        head = TreeNode(preorder[0])
        index_in_inorder = inorder.index(preorder[0])
        inorder_left = inorder[:index_in_inorder]
        inorder_right = inorder[index_in_inorder + 1:]
        if inorder_left and not inorder_right:
            head.left = self.buildTree(preorder[1:], inorder_left)
            head.right = None
        elif inorder_right and not inorder_left:
            head.right = self.buildTree(preorder[1:], inorder_right)
        else:
            head.left = self.buildTree(preorder[1:len(inorder_left) + 1], inorder_left)
            head.right = self.buildTree(preorder[len(inorder_left) + 1:], inorder_right)
        return head
