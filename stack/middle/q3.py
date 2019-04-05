# -*- coding: utf-8 -*-
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
#
# 调用 next() 将返回二叉搜索树中的下一个最小的数。

# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Tree(object):
	def __init__(self):
		self.root = None

	def insert(self, value):
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


class BSTIterator(object):

	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.sort_list = []
		a_stack = []
		tmp = root
		while a_stack or tmp:
			if tmp:
				a_stack.append(tmp)
				tmp = tmp.left
			else:
				tmp = a_stack.pop()
				self.sort_list.append(tmp.val)
				tmp = tmp.right

	def next(self):
		"""
		@return the next smallest number
		:rtype: int
		"""
		if self.sort_list:
			return self.sort_list.pop(0)
		else:
			return None

	def hasNext(self):
		"""
		@return whether we have a next smallest number
		:rtype: bool
		"""
		return len(self.sort_list) > 0


if __name__ == "__main__":
	nodes = [8, 3, 10, 1, 6, 14, 4, 7, 13]
	tree = Tree()
	for node in nodes:
		tree.insert(node)
	root = tree.get_root()
	obj = BSTIterator(root)
	param_1 = obj.next()
	print(param_1)

	param_1 = obj.next()
	print(param_1)

	param_1 = obj.next()
	print(param_1)

	param_1 = obj.next()
	print(param_1)

	param_1 = obj.next()
	print(param_1)

	param_1 = obj.next()

	print(param_1)
	param_2 = obj.hasNext()
	print(param_2)
