# -*- coding: utf-8 -*-
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#     2
#   /   \
#  1     3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 附二叉树的构建过程
# 遍历全部使用迭代算法完成

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


class Solution(object):
	def preTraversal(self, root):
		"""
		前序遍历
		:param root:
		:return:
		"""
		a_list = []
		a_stack = []
		tmp = root
		while tmp or a_stack:
			if tmp:
				a_list.append(tmp.val)
				a_stack.append(tmp)
				tmp = tmp.left
			else:
				tmp = a_stack.pop()
				tmp = tmp.right
		return a_list

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

	def afterTraversal(self, root):
		"""
		后续遍历 左 右 根
		也就是说，，
		:param root:
		:return:
		"""
		a_stack = []
		a_list = []
		a_stack.append(root)
		a_stack.append(root)
		while a_stack:
			p = a_stack[-1]
			a_stack.pop()
			# 第一次弹出，将p的孩子压入栈中
			# 栈中保存的从顶部依次是 left, right, root
			if a_stack and p == a_stack[-1]:
				if p.right:
					a_stack.append(p.right)
					a_stack.append(p.right)
				if p.left:
					a_stack.append(p.left)
					a_stack.append(p.left)
			# 第二次弹出，访问p。
			else:
				a_list.append(p.val)
		return a_list


if __name__ == "__main__":
	nodes = [8, 3, 10, 1, 6, 14, 4, 7, 13]
	tree = Tree()
	for node in nodes:
		tree.insert(node)

	a = Solution().inorderTraversal(tree.get_root())
	print(u"中序遍历是：")
	print(a)

	b = Solution().preTraversal(tree.get_root())
	print(u"前序遍历是：")
	print(b)

	c = Solution().afterTraversal(tree.get_root())
	print(u"后序遍历是：")
	print(c)
