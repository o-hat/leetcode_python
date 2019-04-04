# -*- coding: utf-8 -*-

# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
#
# 示例:
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    a = s.intersection(nums1, nums2)
    print(a)
