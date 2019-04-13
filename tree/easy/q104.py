#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/11 20:29.
"""

# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
from tree.arrTree import create_tree
from tree.treeNode import TreeNode


class Solution(object):
    # 深度优先
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth1(self, root):
        """
        一层一层往栈里塞
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a_stack = [root]
        res = 0
        while a_stack:
            res += 1
            # 不能 for f_node in a_stack  因为一层的循环还没结束 后一层的已经进去了  len(stack) 锁定了一层的数量
            for i in range(len(a_stack)):
                f_node = a_stack.pop(0)
                if f_node.left:
                    a_stack.append(f_node.left)
                if f_node.right:
                    a_stack.append(f_node.right)
        return res


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    tree1 = create_tree(arr1)
    length = Solution().maxDepth1(tree1)
    print length
