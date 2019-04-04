# -*- coding: utf-8 -*-


# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素


class MinStack(object):
	arr = []

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.arr = []

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.arr.append(x)

	def pop(self):
		"""
		:rtype: void
		"""
		self.arr.pop()

	def top(self):
		"""
		:rtype: int
		"""
		return self.arr[len(self.arr) - 1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return min(self.arr)


if __name__ == "__main__":
	minStack = MinStack()
	minStack.push(-2)
	minStack.push(0)
	minStack.push(-3)
	min1 = minStack.getMin()  # ;   --> 返回 -3.
	print(min1)
	minStack.pop()
	top = minStack.top()  # --> 返回 0.
	print(top)
	min2 = minStack.getMin()  # --> 返回 -2.
	print(min2)

