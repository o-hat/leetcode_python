# -*- coding: utf-8 -*-
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
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

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Tree(object):
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


class Solution(object):

	def inorderTraversal(self, root):
		"""
		中序遍历
		:type root: TreeNode
		:rtype: List[int]
		"""
		a_list = []
		a_stack = []
		tmp = root
		while a_stack or tmp:
			if tmp:
				a_stack.append(tmp)
				tmp = tmp.left
			else:
				tmp = a_stack.pop()
				a_list.append(tmp.val)
				tmp = tmp.right
		return a_list


if __name__ == "__main__":
	nodes = [3, 9, 20, None, None, 15, 7]
	tree = Tree()
	for node in nodes:
		tree.insert(node)

	a = Solution().inorderTraversal(tree.get_root())
	print(u"中序遍历是：")
	print(a)
