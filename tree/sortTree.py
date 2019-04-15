#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tree.treeNode import TreeNode


class SortTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        建立排序二叉树
        :param value:
        :return:
        """
        node = TreeNode(value)
        if not self.root:
            self.root = node
        else:
            insert(self.root, node)

    def get_root(self):
        return self.root


def insert(node, new_node):
    if node.val > new_node.val:
        if not node.left:
            node.left = new_node
        else:
            insert(node.left, new_node)
    else:
        if not node.right:
            node.right = new_node
        else:
            insert(node.right, new_node)
