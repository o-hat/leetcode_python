# -*- coding: utf-8 -*-

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 示例 1:
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4

class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums))) * 2 - sum(nums)

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 2, 1]
    nums = [4, 1, 2, 1, 2]
    a = s.singleNumber(nums)
    print(a)
