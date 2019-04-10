# -*- coding: utf-8 -*-

# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串

class Solution(object):
	def scoreOfParentheses(self, S):
		"""
		:type S: str
		:rtype: int
		"""
		stack = []
		for i in range(len(S)):
			if S[i] == "(":
				stack.append("(")
			else:
				count = 0
				node = stack.pop()
				while node != "(":
					if count == 0:
						count = node
					else:
						count += node
					node = stack.pop()
				if count == 0:
					stack.append(1)
				else:
					stack.append(count * 2)
		return sum(stack)


s = "(()(()))"
# 步骤
# s = "(1(()))"
# s = "(1(1))"
# s = "(1 2)"
# s = "(3)"
# s = "6"
a = Solution().scoreOfParentheses(s)
print(a)
