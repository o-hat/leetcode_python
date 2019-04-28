#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/28 19:48.
"""

# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree.treeNode import TreeNode


class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None
		mid = len(nums) // 2
		t = TreeNode(nums[mid])
		t_left = nums[:mid]
		t_right = nums[mid + 1:]
		t.left = self.sortedArrayToBST(t_left)
		t.right = self.sortedArrayToBST(t_right)
		print(t.val)
		return t


if __name__ == "__main__":
	arr = [-10, -3, 0, 5, 9]
	Solution().sortedArrayToBST(arr)
