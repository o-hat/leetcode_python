# -*- coding: utf-8 -*-

# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#
#
# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
#
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
#
# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
#
#
# 提示：
#
# 给定的两颗树可能会有 1 到 100 个结点。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        pass



if __name__ == "__main__":
    s = Solution()
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    # a = s.leafSimilar(nums1, nums2)
    # print(a)
