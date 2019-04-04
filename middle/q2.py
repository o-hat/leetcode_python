#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_len = 0
		a_list = []
		for i in s:
			print("准备判断【%s】,现在是【%s】，最大长度为[%s]" % (i, a_list, max_len))
			if i in a_list:
				if len(a_list) >= max_len:
					max_len = len(a_list)
					# print("重复的是【%s】,索引是【%s】" % (i, index))
				index = a_list.index(i)
				a_list = a_list[index + 1:]
				a_list.append(i)
				print("改变完：【%s】" % a_list)
			else:
				a_list.append(i)
				if len(a_list) > max_len:
					max_len = len(a_list)
		return max(max_len, len(a_list))


# a = Solution().lengthOfLongestSubstring("hkcpmprxxxqw")
a = Solution().lengthOfLongestSubstring("bpfbhmipx")
# a = Solution().lengthOfLongestSubstring("pwwkew")
# a = Solution().lengthOfLongestSubstring("aab")
# a = Solution().lengthOfLongestSubstring("dvdf")
print(a)
