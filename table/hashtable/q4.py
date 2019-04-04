# -*- coding: utf-8 -*-

# 编写一个算法来判断一个数是不是“快乐数”。

# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

# 示例: 

# 输入: 19
# 输出: true
# 解释: 
# 1 + 81 = 82
# 64 + 4 = 68
# 36 + 64 = 100
# 1 + 0 + 0 = 1

# 无限循环的话就会出现重复值  利用这个解题 ！！！！
# 只要是和为4或者为原来的数，则不是快乐数。
import math


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a_set = set()
        while not n == 1:
            if n in a_set:
                return False
            a_set.add(n)
            tmp = 0
            while not n == 0:
                mod = n % 10
                tmp += mod * mod
                n /= 10
            n = tmp
        return True


if __name__ == "__main__":
    s = Solution()
    n = 19
    a = s.isHappy(n)
    print(a)
