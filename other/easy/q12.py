#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
#
# 注意：整数顺序将表示为一个字符串。


class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		return self.cal(n-1, "1")

	def cal(self, n, s):
		if n == 1:
			return s
		else:
			s = ""
			for w in n:
				s += w


a = Solution().countAndSay(1)
print(a)

