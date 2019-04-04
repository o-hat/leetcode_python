#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，"cab"
# 可以写成"-.-..--..."，(即 "-.-." + "-..." + ".-"字符串的结合)。我们将这样一个连接过程称作单词翻译。
# 返回我们可以获得所有词不同单词翻译的数量。
#
# 例如:
# 输入: words = ["gin", "zen", "gig", "msg"]
# 输出: 2
# 解释:
# 各单词翻译如下:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# 共有  2 种不同翻译, "--...-." 和 "--...--.".
#

# 我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，
# 如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。
# 我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。
#
# 现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
#
# 示例 1:
# 输入:
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "abcdefghijklmnopqrstuvwxyz"
# 输出: [3, 60]
# 解释:
# 所有的字符拥有相同的占用单位10。所以书写所有的26个字母，
# 我们需要2个整行和占用60个单位的一行。


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        pass
        dic = {}
        for i in range(26):
            dic[chr(97 + i)] = widths[i]
        row = 1
        large_line = 0
        for c in S:
            large_line += dic[c]
            if large_line > 100:
                row += 1
                large_line = 0
                large_line += dic[c]

        return [row, large_line]


if __name__ == "__main__":
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "bbbcccdddaaa"
    a = Solution().numberOfLines(widths, s)
    print(a)