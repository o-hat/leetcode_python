# -*- coding: utf-8 -*-

#
# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

# 先遍历大数组nums2，首先将第一个元素入栈；
# 继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value键值对，存入HashMap中；
# 当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
# 遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为-1。

class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		"""
		:type findNums: List[int]
		:type nums: List[int]
		:rtype: List[int]
		"""
		stack = []
		dict = {}
		res = []
		for n in nums:
			while len(stack) and stack[-1] < n:
				dict[stack.pop()] = n
			stack.append(n)
		for ii in findNums:
			if ii in dict.keys():
				res.append(dict.get(ii))
			else:
				res.append(-1)
		return res


if __name__ == "__main__":
	nums1 = [1, 3, 5, 2, 4]
	nums2 = [6, 5, 4, 3, 2, 1, 7]
	a = Solution().nextGreaterElement(nums1, nums2)
	print(a)
