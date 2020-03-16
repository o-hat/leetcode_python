#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2020/2/9 21:31.
"""
from typing import List

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		"""
		暴力破解法
		:param nums:
		:return:
		"""
		max_sum = 0
		for start in range(len(nums)):
			total = nums[start]
			for end in range(start + 1, len(nums)):
				total += nums[end]
				if total > max_sum:
					max_sum = total
		return max_sum


if __name__ == "__main__":
	arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	max_sum = Solution().maxSubArray(arr)
	print("total ===== %s" % max_sum)
