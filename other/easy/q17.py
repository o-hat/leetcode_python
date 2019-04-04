#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# 示例 1：
#
# 输入："ab-cd"
# 输出："dc-ba"
# 示例 2：
#
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 示例 3：
#
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        dic_z = []
        s1 = list(S)
        str_z = ""
        for index, s in enumerate(s1):
            if 97 <= ord(s.lower()) <= 97 + 26:
                str_z += s
                dic_z.append({
                    s: index
                })
            s1[index] = s
        a_list = list(str_z)
        a_list.reverse()
        for i, x in enumerate(dic_z):
            for key, value in x.items():
                s1[value] = a_list[i]
        return ''.join(s1)

    def reverseOnlyLetters1(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        i = 0
        j = len(S) - 1
        while i < j:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1

            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1

        return "".join(S)


if __name__ == "__main__":
    import time

    S = "a-bC-dEf-ghIj"
    start_time = time.time()
    a = Solution().reverseOnlyLetters(S)
    end_time = time.time()
    print(a)
    spend_time = end_time - start_time
    print("耗时：%s" % spend_time)

    start_time1 = time.time()
    b = Solution().reverseOnlyLetters1(S)
    end_time1 = time.time()
    spend_time1 = end_time1 - start_time1
    print(b)
    print("耗时：%s" % spend_time1)
