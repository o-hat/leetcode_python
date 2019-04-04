# -*- coding: utf-8 -*-

# 统计所有小于非负整数 n 的质数的数量。
# 示例:
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7
from math import sqrt


class Solution(object):
    # 超时了
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        if n > 1:
            for i in range(2, n):
                if i > 1 and self.is_zhi(i):
                    # print("========%s是质数" % i)
                    total += 1
        return total

    def is_zhi(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n):
        if n < 3:
            return 0
        else:
            arr = [True] * n
            arr[0] = False
            arr[1] = False
            for i in range(2, i*i):
                if not arr[i]:
                    continue
                for j in range(i*i, n):
                    arr[j] = False
                arr[i] = self.is_zhi(i)
            print(arr)


if __name__ == "__main__":
    s = Solution()
    num = 10
    a = s.countPrimes(num)
    print(a)
