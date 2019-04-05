# -*- coding: utf-8 -*-

# 给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。
#
# 从形式上讲，只有满足下面几点之一，括号字符串才是有效的：
#
# 它是一个空字符串，或者
# 它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
# 它可以被写作 (A)，其中 A 是有效字符串。
# 给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

class Solution(object):
	def minAddToMakeValid(self, S):
		n = 0
		"""
		:type S: str
		:rtype: int
		"""
		a_stack = []
		for s in S:
			if a_stack:
				p = a_stack[-1]
				if s == ")" and p == "(":
					a_stack.pop()
					continue
			a_stack.append(s)
		return len(a_stack)


if __name__ == "__main__":
	str = "()))(("
	a = Solution().minAddToMakeValid(str)
	print(a)