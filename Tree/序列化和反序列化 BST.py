# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 15:21
# @Author  : Yippee Song
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def makeBST(data):
    '''
    用int数组构造 BST
    :param data: int数组
    :return: BST
    '''
    if not data:
        return None
    head = TreeNode(data[0])

    def findChild(parent, subs):
        '''
        找出左右子节点的值
        :param parent:
        :param subs:
        :return:
        '''
        left = []
        right = []
        for i in range(len(subs)):
            if subs[i] < parent:
                left.append(subs[i])
            else:
                right.append(subs[i])
        return left, right

    def makeTree(node_root, subs):
        if not subs:
            return
        if subs[0] < node_root.val:
            node_root.left = TreeNode(subs[0])
            parent = node_root.left
        else:
            node_root.right = TreeNode(subs[0])
            parent = node_root.right
        left, right = findChild(parent.val, subs[1:])
        makeTree(parent, left)
        makeTree(parent, right)

    left, right = findChild(head.val, data[1:])
    makeTree(head, left)
    makeTree(head, right)
    return head


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        def preOrder(node):
            ans = []
            ans.append(node.val)
            if node.left:
                ans.extend(preOrder(node.left))
            if node.right:
                ans.extend(preOrder(node.right))
            return ans

        ans = preOrder(root)
        print ans
        return ','.join(map(str, ans))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = map(int, data.split(','))
        head = TreeNode(data[0])

        def findChild(parent, subs):
            left = []
            right = []
            for i in range(len(subs)):
                if subs[i] < parent:
                    left.append(subs[i])
                else:
                    right.append(subs[i])
            return left, right

        def makeTree(node_root, subs):
            if not subs:
                return
            if subs[0] < node_root.val:
                node_root.left = TreeNode(subs[0])
                parent = node_root.left
            else:
                node_root.right = TreeNode(subs[0])
                parent = node_root.right
            left, right = findChild(parent.val, subs[1:])
            makeTree(parent, left)
            makeTree(parent, right)

        left, right = findChild(head.val, data[1:])
        makeTree(head, left)
        makeTree(head, right)
        return head


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    data = [5, 3, 2, 4, 8, 10]
    treeHead = makeBST(data)
    codec = Codec()
    codec.deserialize(codec.serialize(treeHead))
