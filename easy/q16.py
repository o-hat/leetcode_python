#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
#
# 示例 1:
#
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 说明:
#
# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。
# 在真实的面试中遇到过这道题？


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        普通的方法
        """
        n = len(S)
        arr = range(n)
        for index, a in enumerate(S):
            selected = S[index]
            start = index
            if selected == C:
                arr[index] = 0
            else:
                distance = 1
                while True:
                    if start - distance >= 0:
                        pre_s = S[start - distance]
                        if pre_s == C:
                            arr[index] = distance
                            break
                    if start + distance <= n - 1:
                        next_s = S[start + distance]
                        if next_s == C:
                            arr[index] = distance
                            break
                    distance += 1
        return arr


if __name__ == "__main__":
    S = "loveleetcode"
    # S = "lovele"
    C = 'e'
    a = Solution().shortestToChar(S, C)
    print(a)
