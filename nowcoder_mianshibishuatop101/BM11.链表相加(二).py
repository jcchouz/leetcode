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


# 反转列表
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    def calcLen(self, head: ListNode) -> int:
        len = 0
        while head:
            len += 1
            head = head.next
        return len

    def addInList(self, head1: ListNode, head2: ListNode) -> ListNode:
        # write code here
        if not head1 or not head2:
            return head1 if not head2 else head1
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
        len1 = self.calcLen(head1)
        len2 = self.calcLen(head2)
        if len1 < len2:
            head1, head2 = head2, head1
        carry = 0
        tmp = ListNode(0)
        res = head1
        while head1 or head2:
            sum = head1.val + head2.val + carry
            head1.val, carry = sum % 10, sum // 10
            head2 = head2.next if head2.next else tmp
            if not head1.next:
                break
            head1 = head1.next
        if carry:
            head1.next = ListNode(carry)
        return self.reverse(res)


# 辅助栈
class Solution2:
    def addInList(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not head1 or not head2:
            return head1 if not head2 else head1
        s1 = list()
        s2 = list()
        while head1 or head2:
            if head1:
                s1.append(head1)
                head1 = head1.next
            if head2:
                s2.append(head2)
                head2 = head2.next
        node = None
        carry = 0
        while s1 or s2:
            sum = carry
            if s1:
                sum += s1.pop().val
            if s2:
                sum += s2.pop().val
            val, carry = sum % 10, sum // 10
            cur = ListNode(val)
            cur.next = node
            node = cur
        if carry:
            cur = ListNode(carry)
            cur.next = node
        return cur


while True:
    try:
        # 输入输出
        l1, l2 = eval(input())
        head1 = generateLinkedList(l1)
        head2 = generateLinkedList(l2)
        solution = Solution2()
        head_res = solution.addInList(head1, head2)
        res = []
        while head_res:
            res.append(head_res.val)
            head_res = head_res.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
