#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


# 一边遍历
# 从右往左遍历 找到比右边小的
# 然后换位置
# 然后翻转剩下的

#  1 5 8 4 7 5 3 2 1
# 找到 4
# 4 5 换位置
# 翻转 1 5 8 5 1 2 3 4 7

class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		i = n - 2
		while i >= 0 and nums[i + 1] <= nums[i]:
			i -= 1
		print('找到数索引是【%s】,值是【%s】' % (i, nums[i]))
		if i >= 0:
			j = n - 1
			while 0 <= j and nums[j] <= nums[i]:
				j -= 1
			print("找到刚好比那个数小的数是【%s】" % nums[j])
			self.swap_arr(nums, i, j)
		print("交换位置为：%s" % arr)

		print("从位置【%s】开始翻转" % (i + 1))
		self.reverse_arr(nums, i + 1)

	def swap_arr(self, nums, i, j):
		print("i====[%s]  j====[%s]" % (i, j))
		tmp = nums[j]
		nums[j] = nums[i]
		nums[i] = tmp
		return nums

	def reverse_arr(self, nums, i):
		j = len(nums) - 1
		while i < j:
			self.swap_arr(nums, i, j)
			i += 1
			j -= 1
		# print(nums)
		return nums


arr = [1, 5, 8, 4, 7, 5, 3, 2, 1]
# arr = [5, 1, 1]
# arr = [1, 5, 1]
Solution().nextPermutation(arr)
# Solution().reverse_arr(arr,0)
print(arr)
