#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""

# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
#
# 例如，
#
# 给定二叉搜索树:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# 和值: 2
# 你应该返回如下子树:
#
#       2
#      / \
#     1   3
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
from tree.sortTree import SortTree
from tree.treeNode import TreeNode


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root


if __name__ == "__main__":
    nodes = [4, 2, 7, 1, 3]
    tree = SortTree()
    for node in nodes:
        tree.insert(node)
    root = tree.get_root()
    node = Solution().searchBST(root, 6)
    print node
