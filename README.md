## leetcode_python

## 按照数据结构与算法分析目录结构开始刷题  （目录分类名）
- 表
    - hashTable
    - linkTable
- 栈
- 队列
- 树
    - tree
- 散列
- 优先队列（栈）
- 排序
- 不相交集类
- 图论算法
- 算法设计技巧
- 摊还分析
- 高级数据结构及其实现

## 2019-04-05
从原来的项目单独抽离出来，打算从分类的难度一个一个过

## 栈 stack
1. o.isdigit()只能判断整数。判断是否是正负数
```python
def is_number(n):
    try:
        a = int(n)
        return isinstance(a, int)
    except ValueError:
        return False
```

## 树 Tree
> 栈太多题目牵扯到二叉树 所以先写树 再回头写栈的题目： stack /middle/q103、

1. 遍历 ：stack/middle/q2
- 中序遍历： 左->根->右 
- 前序遍历： 根->左->右
- 后序遍历： 左->右->根


2. 树的通用思路
- 使用递归解决
- 使用栈解决

3. 多叉树
```Python
class Node(object):
    def __init__(self,val,children):
        self.val = val
        self.children = children
```
4. 字符串和list翻转
```python
for i in range(5)[::-1]:
    # 4,3,2,1,0
    print(i)
```

5. 高度平衡二叉搜索树  
指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

6. map extend === q257 




