import traceback

"""
头插法，递归，栈
"""


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = head
        for _ in range(1, m):
            pre = cur
            cur = cur.next
        for _ in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return res.next


class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        res = ListNode(-1)
        res.next = head
        l = res
        for _ in range(1, m):
            l = l.next
        start = end = l.next
        for _ in range(m, n):
            end = end.next
        r = end.next
        end.next = None
        pre = r
        while start:
            tmp = start.next
            start.next = pre
            pre = start
            start = tmp
        l.next = end
        return res.next


class Solution3:
    def __init__(self) -> None:
        self.tmp = None

    def reverse(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.tmp = head.next
            return head
        node = self.reverse(head.next, n - 1)
        head.next.next = head
        head.next = self.tmp
        return node

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        if m == 1:
            return self.reverse(head, n)
        node = self.reverseBetween(head.next, m - 1, n - 1)
        head.next = node
        return head


while True:
    try:
        # 输入输出
        lkd_list, m, n = eval(input())
        # .strip().split(",")
        head = None
        if lkd_list:
            head = ListNode(lkd_list[0])
            node = head
        for i in range(1, len(lkd_list)):
            node.next = ListNode(lkd_list[i])
            node = node.next
        solution = Solution3()
        rvs_head = solution.reverseBetween(head, m, n)
        res = list()
        while rvs_head:
            res.append(rvs_head.val)
            rvs_head = rvs_head.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
