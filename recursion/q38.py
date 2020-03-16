#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2020/2/9 20:56.
"""

"""

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

"""


class Solution:
	def countAndSay(self, n: int) -> str:
		"""
		每次都要算一遍
		:param n:
		:return:
		"""
		if n <= 1:
			return "1"
		pre = self.countAndSay(n - 1)
		res = ""
		count = 1
		for i in range(len(pre)):
			if i == 0:
				count = 1
			elif pre[i] != pre[i - 1]:
				tmp = str(count) + pre[i - 1]
				res += tmp
				count = 1
			elif pre[i] == pre[i - 1]:
				count += 1
			if i == len(pre) - 1:
				tmp = str(count) + pre[i]
				res += tmp
		return res


if __name__ == "__main__":
	s = Solution().countAndSay(10)
	print(s)
