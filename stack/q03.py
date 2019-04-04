# -*- coding: utf-8 -*-

# 使用栈实现队列的下列操作：
#
#
# 队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头

# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 示例:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false


class MyQueue(object):
	arr = []

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.arr = []

	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: void
		"""
		self.arr.append(x)

	def pop(self):
		"""
		移除首位
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		if self.arr:
			return self.arr.pop(0)

	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		if self.arr:
			return self.arr[0]

	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return len(self.arr) == 0


if __name__ == "__main__":
	queue = MyQueue()

	# queue.push(1)
	# queue.push(2)
	# a = queue.peek()  # 返回 1
	# print(a)
	b = queue.pop()  # 返回 1
	print(b)
	# c = queue.empty()  # 返回 false
	# print(c)
