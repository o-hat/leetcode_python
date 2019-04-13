## leetcode_python
> 越来越觉得算法重要，所以才开始学 语言使用python 是因为语法简洁、清晰、易懂 
等全部做完可以用js复习一遍

#### 按照数据结构与算法分析目录结构开始刷题  （目录分类名）
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

#### 树 Tree

1. 二叉树利用迭代遍历 ：stack/middle/q2
- 中序遍历： 左->根->右 
- 前序遍历： 根->左->右
- 后序遍历： 左->右->根


2. 栈太多题目牵扯到二叉树 先从简单开始做树，再回头做stack /middle/q103、
- 使用递归解决
- 使用栈解决

3. 多叉树
```Python
class Node(object):
    def __init__(self,val,chirdren):
        self.val = val
        self.children = chirdren
```
4. 字符串和list翻转
```python
for i in range(5)[::-1]:
    # 4,3,2,1,0
    print(i)
```


