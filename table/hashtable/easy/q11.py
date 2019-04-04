# -*- coding: utf-8 -*-

# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set(nums)
        return not (len(set1) == len(nums))

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a_map = {}
        for n in nums:
            if n in a_map.keys():
                return True
            else:
                a_map[n] = 1
        return False


if __name__ == "__main__":
    s = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    a = Solution().containsDuplicate(s)
    print(a)
