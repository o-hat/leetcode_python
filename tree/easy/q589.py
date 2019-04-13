#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""


# 给定一个 N 叉树，返回其节点值的前序遍历。
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
# 返回其前序遍历: [1,3,5,6,2,4]。
# 根-左-右


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def __init__(self):
        self.res = []

    def preorder(self, root):
        """
        递归实现
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        self.res.append(root.val)
        if root.children:
            for i in range(len(root.children)):
                self.preorder(root.children[i])
        return self.res

    def preorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 先判断root是否为空 !!!! 提交了几次才发现
        if not root:
            return []
        a_stack = [root]
        a_list = []
        while a_stack:
            node = a_stack.pop()
            a_list.append(node.val)
            children = node.children
            if children:
                # 反向进栈
                for i in range(len(children))[::-1]:
                    if children[i]:
                        a_stack.append(children[i])
        return a_list


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
    res = Solution().preorder(root)
    print (u"多叉树的前序遍历为==========%s" % res)
