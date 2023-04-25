import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 头插法，递归，栈
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here
        if not head or not head.next or k == 1:
            return head
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = head
        len = 0
        while head:
            len += 1
            head = head.next
        for _ in range(len // k):
            for _ in range(1, k):
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            pre = cur
            cur = cur.next
        return res.next


class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here
        if not head or not head.next or k == 1:
            return head
        len = 0
        node = head
        while node:
            len += 1
            node = node.next
        if len < k:
            return head
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = head
        for _ in range(1, k):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        cur.next = self.reverseKGroup(cur.next, k)
        return res.next


class Solution3:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here
        if not head or not head.next or k == 1:
            return head
        stack = list()
        len = 0
        node = head
        while node:
            len += 1
            node = node.next
        if len < k:
            return head
        res = ListNode(-1)
        res.next = head
        node = res
        for _ in range(len // k):
            for _ in range(k):
                stack.append(head)
                head = head.next
            while stack:
                node.next = stack.pop()
                node = node.next
        node.next = head
        return res.next


while True:
    try:
        # 输入输出
        lkd_list, k = eval(input())
        # .strip().split(",")
        head = None
        if lkd_list:
            head = ListNode(lkd_list[0])
            node = head
        for i in range(1, len(lkd_list)):
            node.next = ListNode(lkd_list[i])
            node = node.next
        solution = Solution3()
        rvs_head = solution.reverseKGroup(head, k)
        res = list()
        while rvs_head:
            res.append(rvs_head.val)
            rvs_head = rvs_head.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
