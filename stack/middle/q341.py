# -*- coding: utf-8 -*-

# 给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
#
# 列表中的项或者为一个整数，或者是另一个列表。
#
# 示例 1:
#
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 示例 2:
#
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,4,6]。

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#
# 	def isInteger(self):
# 		"""
# 		@return True if this NestedInteger holds a single integer, rather than a nested list.
# 		:rtype bool
# 		"""
#
# 	def getInteger(self):
# 		"""
# 		@return the single integer that this NestedInteger holds, if it holds a single integer
# 		Return None if this NestedInteger holds a nested list
# 		:rtype int
# 		"""
#
# 	def getList(self):
# 		"""
# 		@return the nested list that this NestedInteger holds, if it holds a nested list
# 		Return None if this NestedInteger holds a single integer
# 		:rtype List[NestedInteger]
# 		"""

### 通过迭代
# class NestedIterator(object):
#
# 	def __init__(self, nestedList):
# 		"""
# 		Initialize your data structure here.
# 		:type nestedList: List[NestedInteger]
# 		"""
# 		self.nestedList = nestedList
# 		self.it = None
# 		self.current = 0
#
# 	def next(self):
# 		"""
# 		:rtype: int
# 		"""
# 		if self.it:
# 			if self.it.hasNext():
# 				return self.it.next()
# 			else:
# 				self.current += 1
# 				self.it = None
# 		ite = self.nestedList[self.current]
#
# 		if ite.isInteger():
# 			self.current += 1
# 			self.it = None
# 			return ite.getInteger()
# 		else:
# 			self.it = NestedIterator(ite.getList())
# 			return self.it.next()
#
# 	def hasNext(self):
# 		"""
# 		:rtype: bool
# 		"""
# 		if self.it:
# 			if self.it.hasNext():
# 				return True
# 			self.it = None
# 			self.current += 1
# 		if self.current >= len(self.nestedList):
# 			return False
# 		ite = self.nestedList[self.current]
# 		if ite.isInteger():
# 			return True
# 		else:
# 			self.it = NestedIterator(ite.getList())
# 			return self.it.hasNext()

## 两个栈 递归取出
class NestedIterator(object):

	def __init__(self, nestedList):
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
		self.a_stack1 = []
		self.a_stack2 = []

		def letOut(li):
			for l in li:
				if l.isInteger():
					self.a_stack1.append(l.getInteger())
				else:
					letOut(l.getList())

		letOut(nestedList)
		while self.a_stack1:
			self.a_stack2.append(self.a_stack1.pop())

	def next(self):
		"""
		:rtype: int
		"""
		return self.a_stack2.pop()

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return bool(self.a_stack2)


# Your NestedIterator object will be instantiated and called as such:

if __name__ == "__main__":
	pass
# nestedNumList = [1, [4, [6]]]
# nestedList = [NestedInteger(num) for num in nestedNumList]
# i, v = NestedIterator(nestedList), []
# while i.hasNext():
# 	v.append(i.next())
# print(v)
