# -*- coding: utf-8 -*-

# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
# 示例:
#
# 输入：
# s = "abcd"
# t = "abcde"
#
# 输出：
# e
#
# 解释：
# 'e' 是那个被添加的字母。

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum1 = sum([ord(code) for code in s])
        sum2 = sum([ord(code) for code in t])
        return chr(sum2 - sum1)

    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        arr = [ord(code) for code in s + t]
        a = 0
        for num in arr:
            a ^= num
        return chr(a)


if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    a = Solution().findTheDifference(s, t)
    print(a)
