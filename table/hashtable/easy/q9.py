# -*- coding: utf-8 -*-

#  在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
#
# 返回重复了 N 次的那个元素。
# 输入：[1,2,3,3]
# 输出：3

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a_map = {}
        for s in A:
            if s not in a_map:
                a_map[s] = 1
            else:
                return s


if __name__ == "__main__":
    s = [1, 2, 3, 3]
    a = Solution().repeatedNTimes(s)
    print(a)
