#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if not n:
			return 0
		i = 0  # 慢
		j = 1
		while j < n:
			if not nums[j] == nums[i]:
				i += 1
				nums[i] = nums[j]
			j += 1
		return i + 1


Solution().removeDuplicates([1, 1, 2, 3, 4, 5, 6, 6, 7, 7])
# Solution().removeDuplicates([1, 1, 2])
