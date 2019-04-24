#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""

# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
from tree.arrTree import create_tree


class Solution(object):

    def levelOrderBottom1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        a_stack = [root]
        while a_stack:
            tmp = []
            res_each = []
            for node in a_stack:
                res_each.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            a_stack = tmp
            res.insert(0, res_each)
        return res

    def levelOrderBottom(self, root):
        if not root:
            return []
        res = []

        def func(node, level):
            if len(res) <= level:
                res.append([])
            if node:
                res[level].append(node.val)
            if node.left:
                func(node.left, level + 1)
            if node.right:
                func(node.right, level + 1)

        func(root, 0)
        res.reverse()
        return res




if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    root = create_tree(nodes)
    arr = Solution().levelOrderBottom(root)
    print arr
