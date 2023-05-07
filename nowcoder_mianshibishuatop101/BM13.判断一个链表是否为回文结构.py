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
    res = ListNode(-1)
    cur = res
    for val in l:
        cur.next = ListNode(val)
        cur = cur.next
    return res.next


# 快慢指针
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self, head: ListNode) -> bool:
        # write code here
        if not head or not head.next:
            return True
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = slow
        cur = slow.next
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        pre = pre.next
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True


while True:
    try:
        # 输入输出
        l = eval(input())
        head = generateLinkedList(l)
        solution = Solution()
        res = solution.isPail(head)
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
