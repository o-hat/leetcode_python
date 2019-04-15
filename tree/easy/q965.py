#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""

# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
#
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
#
#
#
# 示例 1：
#
#
#
# 输入：[1,1,1,1,1,null,1]
# 输出：true
from tree.arrTree import create_tree


class Solution(object):

    def isUnivalTree(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if (root.left and not (root.val == root.left.val)) or (root.right and not (root.val == root.right.val)):
            return False
        else:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

    def isUnivalTree1(self, root):
        """
        栈
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return None
        a_stack = [root]
        a_list = []
        while a_stack:
            node = a_stack.pop()
            if node.val not in a_list:
                a_list.append(node.val)
            if node.left:
                a_stack.append(node.left)
            if node.right:
                a_stack.append(node.right)
        return len(a_list) == 1


if __name__ == "__main__":
    # nodes = [1, 1, 1, 1, 1, None, 1]
    nodes = [9, 9, 9, 9, 9, 9, 6]
    root = create_tree(nodes)
    flag = Solution().isUnivalTree(root)
    print flag
