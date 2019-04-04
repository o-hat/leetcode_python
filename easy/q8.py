#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 5行 =========>>>>>     [1]     1
# 					   [1][1]      2
#                     [1][2][1]      3
# 在杨辉三角中，每个数是它左上方和右上方的数的和。


class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		arr = []
		for i in range(numRows):
			row = []
			for j in range(i+1):
				if j == 0 or j == i:
					row.append(1)
				else:
					row.append(arr[i-1][j-1] + arr[i-1][j])
			arr.append(row)
		print(arr)

Solution().generate(6)
