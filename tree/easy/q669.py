#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""

# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
#
#    示例 2:
#
# 输入:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# 输出:
#       3
#      /
#    2
#   /
#  1
from tree.sortTree import SortTree


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            # 小了 用右节点代替
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        # 小了 用右节点代替(如果是叶子节点 且符合条件 返回叶子节点)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


if __name__ == "__main__":
    # arr = [3, 0, 4, 2, 1]
    arr = [0, 2, 1]
    tree = SortTree()
    for a in arr:
        tree.insert(a)
    root = tree.get_root()
    node = Solution().trimBST(root, 1, 3)
    print "done"
