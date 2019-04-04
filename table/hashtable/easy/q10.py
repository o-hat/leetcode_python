# -*- coding: utf-8 -*-

#  给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#  ["Hello", "Alaska", "Dad", "Peace"]
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a_map = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2,
                 'f': 2,
                 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
        res = []
        for w in words:
            tmp = a_map.get(w[0].lower())
            is_right = True
            for c in w[1:]:
                if not tmp == a_map.get(c.lower()):
                    is_right = False
                    break
            if is_right:
                res.append(w)
        return res


if __name__ == "__main__":
    s = ["Hello", "Alaska", "Dad", "Peace"]
    a = Solution().findWords(s)
    print(a)
