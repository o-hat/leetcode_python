#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

u"""
讲一个32位的带符号的整数翻转

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0

"""


class Solution(object):

	def reverse(self, num):
		"""
		时间复杂度：O(\log(x))O(log(x))，xx 中大约有 \log_{10}(x)log 10 (x) 位数字。
		空间复杂度：O(1)O(1)。
		python的最大值和最小值  报错
		:param num:
		:return:
		"""
		print("开始前:%s" % num)
		rev = 0
		while not num == 0:
			first = num % 10
			last = num / 10
			if rev > sys.maxint or (rev == sys.maxint / 10 and first > 7):
				return 0
			if rev < sys.minint or (rev == sys.minint / 10 and first < -8):
				return 0
			rev = last * 10 + first
		return rev

	def reverse1(self, x):
		"""
		解法1
		:param x:
		:return:
		"""
		a = False
		if x < 0:
			x = -x
			a = True
		x = str(x)
		arr = list(x)
		reverse_arr = [str(x) for x in arr]
		reverse_arr.reverse()
		res_str = "".join(reverse_arr)
		num = -int(res_str) if a else int(res_str)
		print(2**31 - 1)
		if num < -2**31 or num > (2**31 - 1):
			return 0
		else:
			return num


if __name__ == "__main__":
	solution = Solution()
	num = solution.reverse1(1534236469)
	print("结果：%s" % num)
