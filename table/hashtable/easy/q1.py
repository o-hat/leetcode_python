# -*- coding: utf-8 -*-

# 集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
# 示例 1:
#
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
#
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。


class Solution(object):
    def findErrorNums_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        超过时间限制
        """
        pass
        dict = {}
        res = []
        for n in nums:
            if n not in dict.keys():
                dict[n] = 1
            else:
                res.append(n)
        m = len(nums)
        for i in range(1, m + 1):
            if i not in dict.keys():
                res.append(i)
        return res

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        m = len(nums)
        s2 = (1 + m) * m / 2
        s1 = sum(set(nums))
        s = sum(nums)
        res.append(s - s1)
        res.append(s2 - s1)
        return res


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 4]
    a = s.findErrorNums(nums1)
    print(a)
