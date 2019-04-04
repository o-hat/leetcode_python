# -*- coding: utf-8 -*-

# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
#
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。
# 示例：
# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
# 提示：
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

# &运算： 两个数都转为二进制，然后从高位开始比较，如果两个数都为1则为1，否则为0。
# 6&1 === 》  1100 比 0001  =====》》  0  ====== 》》》  可以用来判断是否是奇数  如果为0 就是偶数
# 9&1  1 0010 比 1 ===》 1

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = [0] * n
        j = 1
        o = 0
        for i in A:
            if i % 2 == 0:
                res[o] = i
                o += 2
            else:
                res[j] = i
                j += 2
        return res

    def sortArrayByParityII2(self, A):
        """
        更优解：循环的时候直接判断偶数位置是不是偶数
        不是的话 找到一个奇数位的偶数去替换
        报错了！！！！ j out of index 下标越界了
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        j = 1
        for i in range(0, n, 2):
            if A[i] % 2 == 0:
                while A[j] % 2 == 0:
                    j += 2
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
        return A

    def sortArrayByParityII3(self, A):
        """
        这种最垃圾
        :type A: List[int]
        :rtype: List[int]
        """
        ou = [i for i in A if i % 2]
        ji = [i for i in A if not i % 2]
        return [i for n in zip(ji, ou) for i in n]


if __name__ == "__main__":
    s = Solution()
    nums = [9, 4, 9, 8, 4, 5]
    a = s.sortArrayByParityII2(nums)
    print(a)
