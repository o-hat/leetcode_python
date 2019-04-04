## leetcode_python

#### 按照数据结构与算法分析目录结构开始刷题  （目录分类名）
- 表
    - hashTable
    - linkTable
- 栈
- 队列
- 树
- 散列
- 优先队列（栈）
- 排序
- 不相交集类
- 图论算法
- 算法设计技巧
- 摊还分析
- 高级数据结构及其实现

#### 2019-04-05
从原来的项目单独抽离出来，打算从分类的难度一个一个过

#### 栈 stack
1. o.isdigit()只能判断整数。判断是否是正负数
```python
def is_number(n):
    try:
        a = int(n)
        return isinstance(a, int)
    except ValueError:
        return False
```
2. 中序遍历:依据层次遍历二叉树 stack/middle/q2

#### 二叉树
