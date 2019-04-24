#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""
from __future__ import division

# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
#
# 示例 1:
#
# 输入:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
from tree.arrTree import create_tree

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res = []
        a_stack = [root]
        while a_stack:
            tmp = []
            total = 0
            for node in a_stack:
                if node:
                    total += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(total / len(a_stack))
            a_stack = tmp
        return res


if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    root = create_tree(nodes)
    arr = Solution().averageOfLevels(root)
    print arr
