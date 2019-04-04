# -*- coding: utf-8 -*-

# 使用队列实现栈的下列操作：
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。


class MyStack(object):
	arr = []

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.arr = []

	def push(self, x):
		"""
		Push element x onto stack.
		:type x: int
		:rtype: void
		"""
		self.arr.append(x)

	def pop(self):
		"""
		Removes the element on top of the stack and returns that element.
		:rtype: int
		"""
		return self.arr.pop()

	def top(self):
		"""
		Get the top element.
		:rtype: int
		"""
		return self.arr[len(self.arr) - 1]

	def empty(self):
		"""
		Returns whether the stack is empty.
		:rtype: bool
		"""
		return len(self.arr) == 0


if __name__ == "__main__":
	minStack = MyStack()
	minStack.push(-2)
	minStack.push(0)
	minStack.push(-3)
	minStack.pop()
	print(minStack)
	print(minStack.top())
	print(minStack.empty())
