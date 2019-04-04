#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
import math


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        while i >= -len(digits) - 1:
            first = digits[i] if i > -len(digits) else 0
            if first + 1 < 10:
                sub_list = digits[i:]
                sub_list = [str(x) for x in sub_list]
                num = int(''.join(sub_list))
                digits[i:] = [int(x) for x in list(str(num + 1))]
                return digits
            else:
                i -= 1


# def plusOne(self, digits):
# 	"""
# 	:type digits: List[int]
# 	:rtype: List[int]
# 	"""
# 	n = len(digits)
# 	total = 0
# 	for index, num in enumerate(digits):
# 		total += num * math.pow(10, n - index - 1)
# 	return [int(x) for x in list(str(int(total + 1)))]


arr = [9, 1, 2, 3, 4, 5, 9]
# arr = [9, 9, 9]
a = Solution().plusOne(arr)
print(a)
