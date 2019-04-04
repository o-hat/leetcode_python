#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5


##  split（" "）切（"a "）  传入空格切  返回['a','']
##  split（）切（"a "）  返回['a']


class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		strList = s.split()
		print(strList)
		if strList:
			return len(strList[-1])
		return 0


a = Solution().lengthOfLastWord('a  ')
print(a)
