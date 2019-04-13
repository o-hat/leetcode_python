#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/4/13 17:37.
"""
from tree.treeNode import TreeNode


# 把树从根左右的顺序从0开始标号。那么第i号节点的左孩子的标号是2*i+1,右孩子是2*i+2。
def create_tree(arr):
    """
    通过数组建立二叉树
    :param arr:
    :return:
    """
    nodelist = []
    if arr:
        length = len(arr)
        for val in arr:
            node = TreeNode(val) if val else None
            nodelist.append(node)
        i = 0
        while i <= length / 2 + 1:
            left = 2 * i + 1
            right = 2 * i + 2
            while not arr[i]:
                i += 1
            if left < length:
                if nodelist[i]:
                    nodelist[i].left = nodelist[left]
            if right < length:
                if nodelist[i]:
                    nodelist[i].right = nodelist[right]
            i += 1

        return nodelist[0]
    return None


if __name__ == "__main__":
    pass
    arr = [1, 2, 3, 4, 5, 6]
    root = create_tree(arr)
    print "done"
