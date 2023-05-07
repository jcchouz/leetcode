import traceback
from typing import List


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


def generateLinkedList(l: List[int]) -> ListNode:
    if not l:
        return None
    res = ListNode(-1)
    cur = res
    for val in l:
        cur.next = ListNode(val)
        cur = cur.next
    return res.next


# 归并排序
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        l = self.sortInList(head)
        r = self.sortInList(head2)
        res = ListNode(-1)
        cur = res
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l if l else r
        return res.next


class Solution2:
    def sortInList(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        tmp = list()
        while head:
            tmp.append(head.val)
            head = head.next
        tmp.sort()
        res = ListNode(-1)
        cur = res
        for val in tmp:
            cur.next = ListNode(val)
            cur = cur.next
        return res.next


while True:
    try:
        # 输入输出
        l = eval(input())
        head = generateLinkedList(l)
        solution = Solution()
        head_res = solution.sortInList(head)
        res = []
        while head_res:
            res.append(head_res.val)
            head_res = head_res.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
