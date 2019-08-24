# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode or None:
        if not head:
            return None
        cur, pre = head, None
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        print_linkedList(cur)

        tail, start = cur, pre

        while n:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1

        if start:
            start.next = pre
        else:
            head = pre
        tail.next = cur
        return head

def print_linkedList(head: ListNode):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


if __name__ == "__main__":
    node_list = []
    arr = [1, 2, 3, 4, 5, 6]
    for a in arr:
        node = ListNode(a)
        node_list.append(node)

    n = len(node_list)
    for index, node in enumerate(node_list):
        if index + 1 < n:
            node.next = node_list[index + 1]
        else:
            node.next = None

    head = node_list[0]
    # print_linkedList(head)
    new_head = Solution().reverseBetween(head, 2, 5)
    print_linkedList(new_head)
