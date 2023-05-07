from calendar import c
from email.quoprimime import header_decode
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


# 双指针
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        tmp = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = tmp
        return head


def printListNode(head: ListNode) -> list:
    res = list()
    while head:
        res.append(head.val)
        head = head.next
    return res


while True:
    try:
        # 输入输出
        l = eval(input())
        head = generateLinkedList(l)
        solution = Solution()
        res = printListNode(solution.oddEvenList(head))
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
