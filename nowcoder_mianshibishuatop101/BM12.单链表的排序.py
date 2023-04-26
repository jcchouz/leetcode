from calendar import c
import traceback
from typing import List


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


def generateLinkedList(l: List[int]) -> ListNode:
    if not l:
        return None
    head = ListNode(l[0])
    cur = head
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return head


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
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        l = self.sortInList(head)
        r = self.sortInList(head2)
        res = ListNode(-1)
        cur = res
        # while l and r:
        #     if l.val<r.val:
        #         cur.
        pass


while True:
    try:
        # 输入输出
        l1, l2 = eval(input())
        head1 = generateLinkedList(l1)
        head2 = generateLinkedList(l2)
        solution = Solution()
        head_res = solution.addInList(head1, head2)
        res = []
        while head_res:
            res.append(head_res.val)
            head_res = head_res.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
