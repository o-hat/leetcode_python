#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。
# （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree.arrTree import create_tree


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def inner(node, level):
            if not node:
                return []
            if len(res) <= level:
                res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            if node.left:
                inner(node.left, level + 1)
            if node.right:
                inner(node.right, level + 1)

        inner(root, 0)
        return res


if __name__ == "__main__":
    arr = [3, 9, 20, None, None, 15, 7]
    root = create_tree(arr)
    res = Solution().zigzagLevelOrder(root)
    print res
