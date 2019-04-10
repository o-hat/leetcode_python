#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/10 10:39.
"""


# 给定有效字符串 "abc"。
#
# 对于任何有效的字符串 V，我们可以将 V 分成两个部分 X 和 Y，使得 X + Y（X 与 Y 连接）等于 V。（X 或 Y 可以为空。）那么，X + "abc" + Y 也同样是有效的。
#
# 例如，如果 S = "abc"，则有效字符串的示例是："abc"，"aabcbc"，"abcabc"，"abcabcababcc"。无效字符串的示例是："abccba"，"ab"，"cababc"，"bac"。
#
# 如果给定字符串 S 有效，则返回 true；否则，返回 false。
#
#
#
# 示例 1：
#
# 输入："aabcbc"
# 输出：true
# 解释：
# 从有效字符串 "abc" 开始。
# 然后我们可以在 "a" 和 "bc" 之间插入另一个 "abc"，产生 "a" + "abc" + "bc"，即 "aabcbc"。

## 用替换的方法
class Solution1(object):
	def isValid(self, S):
		"""
		:type S: str
		:rtype: bool
		"""
		while S.find("abc") > -1:
			S = S.replace("abc", '')
		return not bool(len(S))


## 用栈的方法
class Solution(object):
	def isValid(self, S):
		"""
		:type S: str
		:rtype: bool
		"""
		a_stack = []
		for i in range(len(S)):
			s = S[i]
			if s == "c":
				if len(a_stack) >= 2:
					first = a_stack.pop()
					second = a_stack.pop()
					if not (first == "b" and second == "a"):
						return False
				else:
					return False
			else:
				a_stack.append(s)
		return len(a_stack) == 0


a = Solution().isValid("aabcbc")
# a = Solution().isValid("abccba")
print(a)
