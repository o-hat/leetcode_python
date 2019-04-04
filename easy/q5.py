#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

输入: ["flower","flow","flight"]
输出: "fl"
"""


class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if "" in strs:
			return ''
		n = len(strs)
		pre = ''
		if n > 1:
			for (index, item) in enumerate(strs[0]):
				pre += item
				# print(pre)
				for j in range(1, n):
					flag = pre == strs[j][:index + 1]
					if not flag:
						break
					continue
				if not flag:
					return pre[:-1]
				continue
			return pre
		else:
			return '' if n == 0 else strs[0]


if __name__ == "__main__":
	solution = Solution()
	strs = ["aa", "ab"]
	a = solution.longestCommonPrefix(strs)
	print(a)
