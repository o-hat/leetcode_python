#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		for h in board:
			a = self.validate_hang(h)
			if not a:
				return False
		s_map = {}
		b_map = {}
		for i in range(9):
			s_map[i] = []
			b_map[i] = []
		for index, arr in enumerate(board):
			for a_i, a in enumerate(arr):
				if not a == ".":
					s_map[a_i].append(a)
					# 这个是个大坑 5 / 3 * 3 = 3
					b_key = index / 3 * 3 + a_i / 3
					b_map[b_key].append(a)
		for v in s_map.values():
			r = self.validate_hang(v)
			if not r:
				return False
		for v in b_map.values():
			r = self.validate_hang(v)
			if not r:
				return False
		return True

	def validate_hang(self, item):
		arr = []
		for i in item:
			if not i == ".":
				if i in arr:
					print(i + "      " + str(item))
					return False
				else:
					arr.append(i)
		return True


# arr = [
# 	["5", "3", ".", ".", "7", ".", ".", ".", "."],
# 	["6", ".", ".", "1", "9", "5", ".", ".", "."],
# 	[".", "9", "8", ".", ".", ".", ".", "6", "."],
# 	["8", ".", ".", ".", "6", ".", ".", ".", "3"],
# 	["4", ".", ".", "8", ".", "3", ".", ".", "1"],
# 	["7", ".", ".", ".", "2", ".", ".", ".", "6"],
# 	[".", "6", ".", ".", ".", ".", "2", "8", "."],
# 	[".", ".", ".", "4", "1", "9", ".", ".", "5"],
# 	[".", ".", ".", ".", "8", ".", ".", "7", "9"]
# 	# 	0 - 8
# ]
arr = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
       [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
       ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
       [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

a = Solution().isValidSudoku(arr)
print(a)
