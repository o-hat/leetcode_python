# -*- coding: utf-8 -*-

# 我们把符合下列属性的数组 A 称作山脉：
#
# A.length >= 3
# 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

# 输入：[0,2,1,0]
# 输出：1

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        n = len(A) - 1
        while l < n:
            m = (l + n) / 2
            if A[m] > A[m - 1] and A[m] > A[m + 1]:
                return m
            elif A[m - 1] > A[m] > A[m + 1]:
                n = m
            elif A[m - 1] < A[m] < A[m + 1]:
                l = m
            else:
                return -1
        return -1


if __name__ == "__main__":
    s = Solution()
    nums1 = [3, 4, 5, 1]
    a = s.peakIndexInMountainArray(nums1)
    print(a)
