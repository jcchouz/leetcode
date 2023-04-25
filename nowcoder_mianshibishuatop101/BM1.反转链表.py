import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre


class Solution2:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        if not head:
            return None
        stack = list()
        while head:
            stack.append(head.val)
            head = head.next
        rvs_head = ListNode(stack.pop())
        node = rvs_head
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next
        return rvs_head


class Solution3:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        node = head.next
        rvs_head = self.ReverseList(node)
        node.next = head
        head.next = None
        return rvs_head


while True:
    try:
        # 输入输出
        lkd_list = eval(input())
        # .strip().split(",")
        head = None
        if lkd_list:
            head = ListNode(lkd_list[0])
            node = head
        for i in range(1, len(lkd_list)):
            node.next = ListNode(lkd_list[i])
            node = node.next
        solution = Solution3()
        rvs_head = solution.ReverseList(head)
        res = list()
        while rvs_head:
            res.append(rvs_head.val)
            rvs_head = rvs_head.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
