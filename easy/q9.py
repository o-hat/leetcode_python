#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 二分法


class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		low = 0
		heigh = len(nums)
		while low < heigh:
			mid = low + (heigh - low) / 2
			if nums[mid] > target:
				heigh = mid
			elif nums[mid] < target:
				low = mid + 1
			else:
				return mid
		return low


a = Solution().searchInsert([1, 3, 4, 6, 7], 5)
print(a)
