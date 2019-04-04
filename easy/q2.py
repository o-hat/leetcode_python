#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
-1111 => 1111- false

不转成str做
"""
import copy

class Solution(object):
	"""
	is 用来判断是否是同一个对象
	== 判断值
	"""
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		翻转一半！！！！！

		"""
		# x为0
		if x < 0 or (x % 10 ==0 and not x == 0):
			return False
		half = 0
		while x > half:
			half = half * 10 + x % 10
			x /= 10
		# 当数字长度为奇数时，我们可以通过 revertedNumber / 10 去除处于中位的数字。
		# 例如，当输入为 12321 时，在
		# while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
		# 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
		return half == x or half == x / 10

	def isPalindrome1(self, x):
		"""
		:type x: int
		:rtype: bool
		转成字符串
		一边翻一边比
		"""
		if x < 0:
			return False
		arr = list(str(x))
		length = len(arr)
		if length == 1:
			return True
		for i, n in enumerate(arr):
			if i < length/2:
				if n == arr[length-1-i]:
					continue
				else:
					return False
			return True


if __name__ == "__main__":
	solution = Solution()
	flag = solution.isPalindrome(123123123)
	print("结果：%s" % flag)
