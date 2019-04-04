# -*- coding: utf-8 -*-

# 给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。
#
# 比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5, []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。
#
# 现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。
#
# 示例 1:
#
# 输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# 输出: 11
# 解释:
# 员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
# 注意:
#
# 一个员工最多有一个直系领导，但是可以有多个直系下属
# 员工数量不超过2000。

# Employee info
from collections import deque


class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance1(self, employees, id):
        """
        正常的方法
        :param employees:
        :param id:
        :return:
        """
        # 生成id： Employee的map
        i_map = {e.id: e for e in employees}
        # 访问过的下属 避免重复计算
        visited = set()
        d = deque()
        d.append(i_map[id])
        res = 0
        while d:
            current = d.popleft()
            res += current.importance
            visited.add(current.id)
            for sub in current.subordinates:
                if sub not in visited:
                    d.append(i_map[sub])
        return res

    def getImportance(self, employees, id):
        """
        深度优先 递归
        :param employees:
        :param id:
        :return:
        """
        i_map = {e.id: e for e in employees}

        def dfs(id):
            item = i_map[id]
            res = item.importance
            for sub in item.subordinates:
                res += dfs(sub)
            return res

        return dfs(id)


if __name__ == "__main__":
    s = Solution()
    # employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    employees = [[1, 5, [2, 3]], [2, 3, [4]], [3, 4, []], [4, 1, []]]
    arr = []
    for i in employees:
        arr.append(Employee(i[0], i[1], i[2]))
    id = 1
    a = s.getImportance(arr, id)
    print(a)
