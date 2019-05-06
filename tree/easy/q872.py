#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#      3
#   5     1
# 6  2   9 8
#   7 4
#
#
# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
#
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
#
# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

from tree.arrTree import create_tree
from tree.treeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        a1 = self.get_child_arr(root1)
        a2 = self.get_child_arr(root2)
        return a1 == a2

    def get_child_arr(self, root):
        if not root:
            return []
        a_stack = [root]
        res = []
        while a_stack:
            p = a_stack.pop()
            if p.left:
                a_stack.append(p.left)
            if p.right:
                a_stack.append(p.right)
            if not (p.right or p.left):
                res.append(p.val)
        return res


if __name__ == "__main__":
    arr1 = [1, 2, 3, None, 5]
    tree1 = create_tree(arr1)
    # arr = Solution().leafSimilar(tree1)
    arr = Solution().get_child_arr(tree1)
    print arr
