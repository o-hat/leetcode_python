# -*- coding: utf-8 -*-

#
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
# 示例 1：
#
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。

class Solution(object):
	def backspaceCompare(self, S, T):
		"""
		:type S: str
		:type T: str
		:rtype: bool
		"""
		pass
		a = self.get_res(S)
		b = self.get_res(T)
		return a == b

	def get_res(self, arr):
		stack = []
		for i in arr:
			if i == "#":
				if len(stack):
					stack.pop()
			else:
				stack.append(i)
		return str(stack)


if __name__ == "__main__":
	S = "ab#c"
	T = "ad#c"
	a = Solution().backspaceCompare(S, T)
	print(a)
