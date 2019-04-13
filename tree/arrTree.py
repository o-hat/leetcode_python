#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/13 17:37.
"""
from tree.treeNode import TreeNode


class arrTree(object):

	def __init__(self):
		self.root = None

	def add(self, node):
		if not self.root:
			self.root = node
		else:
			add_node(self.root, node)

	def get_root(self):
		return self.root


def add_node(node, new_node):
	pass


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6]
	tree = arrTree()
	for a in arr:
		node = TreeNode(a)
		tree.add(node)
	root = tree.get_root()
