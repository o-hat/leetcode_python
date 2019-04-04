# -*- coding: utf-8 -*-

# 爱丽丝有一手（hand）由整数数组给定的牌。
# 现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。
# 如果她可以完成分组就返回 true，否则返回 false。
#
# 示例 1：
#
# 输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
# 输出：true
# 解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
# 示例 2：
#
# 输入：hand = [1,2,3,4,5], W = 4
# 输出：false
# 解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。
from collections import Counter


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if not n % W == 0:
            return False
        dict = Counter(hand)
        print dict
        li = sorted(dict)
        print li
        while li:
            a = li[0]
            for i in range(W):
                next = a + i
                if next not in dict:
                    return False
                if dict[next] == 1:
                    dict.pop(next)
                    li.remove(next)
                else:
                    dict[next] -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    w = 3
    a = s.isNStraightHand(hand, w)
    print(a)
