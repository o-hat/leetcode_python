#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

!!!!!!!!!!  空间换时间  hashMap  也就是python里的字典
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        时间太长了
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                if target == n + m:
                    return [i, j]
                else:
                    continue


    def twoSum1(self, nums, target):
        """
        空间换时间
        一遍查找
        :param nums:
        :param target:
        :return:
        """
        hash_map = {}
        for index, n in enumerate(nums):
            if hash_map.has_key(target - n):
                return [hash_map.get(target - n), index]
            else:
                hash_map[n] = index


if __name__ == "__main__":
    solution = Solution()
    num = solution.twoSum1([3,2,4],6)
    print("结果：%s" % num)
