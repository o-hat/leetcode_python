#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		n = len(nums)
		if val not in nums:
			return n
		j = 0
		i = 0
		while j < n:
			if nums[j] != val:
				nums[i] = nums[j]
				i += 1
			j += 1
		print(i)


Solution().removeElement([1, 1, 2, 3, 4, 5, 6, 6, 7, 7], 1)
# Solution().removeDuplicates([1, 1, 2])
