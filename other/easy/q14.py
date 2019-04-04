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
# 注意: 单词列表words的长度不会超过100。
# 每个单词words[i]的长度范围为[1, 12]。
# 每个单词words[i]只包含小写字母。


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        # a = 97
        # a = ord('a')
        result = []
        dic = {}
        for i in range(26):
            dic[chr(97 + i)] = arr[i]
        print(dic)
        for w in words:
            s = ""
            for c in w:
                s += dic[c.lower()]
            if s not in result:
                result.append(s)
        return len(result)


if __name__ == "__main__":
    words = ["gin", "zen", "gig", "msg"]
    a = Solution().uniqueMorseRepresentations(words)
    print(a)