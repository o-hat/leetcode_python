#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""


# 给定一个 N 叉树，返回其节点值的后序遍历。
#
# 例如，给定一个 3叉树 :
#
#      1
#   / \  \
#  3   2   4
#  /\
# 5  6
#
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def __str__(self):
        return self.val


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        def helper(arr, node, level):
            if not node:
                return
            if level >= len(arr):
                arr.append([])
            arr[level].append(node.val)
            for child in node.children:
                helper(arr, child, level + 1)

        res = []
        helper(res, root, 0)
        return res


if __name__ == "__main__":
    arr = [1, 3, 2, 4, 5, 6]
    children_indexes = [[1, 2, 3], [4, 5], [], [], [], []]
    nodelist = []
    # 先初始化全部节点
    for i in range(len(arr)):
        node = Node(arr[i], [])
        nodelist.append(node)
    # 根据子节点数组构建多叉树
    for j in range(len(children_indexes)):
        indexes = children_indexes[j]
        item_node = nodelist[j]
        for index in indexes:
            item_node.children.append(nodelist[index])
    root = nodelist[0]
    res = Solution().levelOrder(root)
    print (u"层次遍历为==========%s" % res)
