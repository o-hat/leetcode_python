#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
True:(){}[] 、 （{[]}） 为空
False  括号出现交叉
"""


class Solution(object):
    def isValid(self, s):
        def validate(a,b):
            return (a == '(' and b ==')') or (a == '[' and b ==']') or (a == '{' and b =='}')
        arr = []
        for i in s:
            if not len(arr):
                arr.append(i)
            elif validate(arr[-1],i):
                arr.pop()
            else:
                arr.append(i)
        return len(arr) == 0

if __name__ == "__main__":
	solution = Solution()
	f = solution.isValid('()')
	print(f)