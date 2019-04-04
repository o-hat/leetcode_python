# -*- coding: utf-8 -*-

#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


class Solution(object):

    def isValid(self, s):
        a_map = {
        	'(': ')',
        	'{': '}',
        	'[': ']'
        }
        arr = []
        for ss in s:
            if ss in a_map.keys():
                arr.append(ss)
            else:
                if not arr:
                    return False
                now = arr.pop()
                if a_map.get(now) == ss:
                    continue
                else:
                    return False
        if len(arr) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    a = "([)]"
    b = Solution().isValid(a)
    print(b)
