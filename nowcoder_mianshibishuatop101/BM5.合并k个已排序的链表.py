import heapq
import traceback
from typing import List


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 顺序合并，双指针+分治
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # write code here
        return self.divideMerge(lists, 0, len(lists) - 1)

    def divideMerge(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = (l + r) // 2
        return self.merge2(
            self.divideMerge(lists, l, mid), self.divideMerge(lists, mid + 1, r)
        )

    def merge2(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if not pHead1 or not pHead2:
            return pHead1 if not pHead2 else pHead2
        res = ListNode(-1)
        cur = res
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2
        return res.next


# 列表
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # write code here
        tmp = []
        for head in lists:
            while head:
                tmp.append(head.val)
                head = head.next
        if not tmp:
            return None
        tmp.sort()
        head = ListNode(tmp[0])
        cur = head
        for i in range(1, len(tmp)):
            cur.next = ListNode(tmp[i])
            cur = cur.next
        return head


# 优先队列，最小堆
class Solution3:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # write code here
        res = ListNode(-1)
        cur = res
        heap = list()
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i))
                lists[i] = lists[i].next
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return res.next


while True:
    try:
        # 输入输出
        lkd_lists = eval(input())
        lists = list()
        for i in range(len(lkd_lists)):
            if not lkd_lists[i]:
                continue
            head = ListNode(lkd_lists[i][0])
            cur = head
            for j in range(1, len(lkd_lists[i])):
                cur.next = ListNode(lkd_lists[i][j])
                cur = cur.next
            lists.append(head)
        solution = Solution3()
        head = solution.mergeKLists(lists)
        res = list()
        while head:
            res.append(head.val)
            head = head.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
