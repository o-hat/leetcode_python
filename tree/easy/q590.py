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
# 返回其前序遍历:[5,6,3,2,4,1].
# 左-右-根


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def __str__(self):
        return self.val


class Solution(object):

    def __init__(self):
        self.res = []

    def postorder(self, root):
        if not root:
            return None
        if root.children:
            for i in range(len(root.children)):
                self.postorder(root.children[i])
        self.res.append(root.val)
        return self.res

    def postorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        a_stack = [root]
        a_list = []
        while a_stack:
            node = a_stack.pop()
            if node.children:
                for i in range(len(node.children)):
                    child = node.children[i]
                    a_stack.append(child)
            a_list.append(node.val)
        return a_list[::-1]



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
    res = Solution().postorder(root)
    print (u"多叉树的后序遍历为==========%s" % res)
