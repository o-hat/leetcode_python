#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

from tree.arrTree import create_tree
from tree.treeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not (root.left or root.right):
            return [str(root.val)]
        res = []
        if root.left:
            res.extend(map(lambda x: "%s->%s" % (root.val, x), self.binaryTreePaths(root.left)))
        if root.right:
            res.extend(map(lambda x: "%s->%s" % (root.val, x), self.binaryTreePaths(root.right)))
        return res


if __name__ == "__main__":
    arr1 = [1, 2, 3, None, 5]
    tree1 = create_tree(arr1)
    arr = Solution().binaryTreePaths(tree1)
    print arr
