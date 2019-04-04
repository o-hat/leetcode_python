#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1  字符串为空 返回0。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2


##  直接拿全部的去匹配



class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		n1 = len(haystack)
		n2 = len(needle)
		if n2 == 0:
			return 0
		if n1 == 0:
			return -1
		if n2 > n1:
			return -1
		for i in range(n1):
			if haystack[i:i+n2] == needle:
				return i
		return -1



a = Solution().strStr('hello', 'll')
# a = Solution().strStr('aaaaa', 'bba')
print(a)
