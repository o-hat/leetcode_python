#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""

罗马数字包含以下七种字符：I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

！！！！！！！！！！！
字典排序返回的是元组  所以手动排了个序。。。。。
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        I(1)， V(5)， X(10)， L(50)，C(100)，D(500) 和 M(1000)。
        只存在这些情况 才在左边
        I + v or x == 4 or 9
        X + L or C == 40 or 90
        c + D or M == 400 or 900
        其他的都在左边
        """
        # array_list = list(s)
        num = 0
        hash_map = {
            "CM": 900,
            "CD": 400,
            "XL": 40,
            "XC": 90,
            "IX": 9,
            "IV": 4,
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        array_list = ["CM", "CD", "XL", "XC", "IX", "IV", "M", "D", "C", "L", "X", "V", "I"]
        i = 0
        while len(s) > 0:
            for k in array_list:
                if s.startswith(k):
                    s = s[len(k):]
                    num += hash_map.get(k)
                    break
                else:
                    i += 1
        return num


if __name__ == "__main__":
    solution = Solution()
    num = solution.romanToInt("MCMXCIV")
    print("结果：%s" % num)
