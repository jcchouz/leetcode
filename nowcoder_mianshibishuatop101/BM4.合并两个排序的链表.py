from cmath import phase
import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
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


class Solution2:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if not pHead1 or not pHead2:
            return pHead1 if not pHead2 else pHead2
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


while True:
    try:
        # 输入输出
        lkd_list1, lkd_list2 = eval(input())
        # .strip().split(",")
        pHead1 = None
        if lkd_list1:
            pHead1 = ListNode(lkd_list1[0])
            node = pHead1
        for i in range(1, len(lkd_list1)):
            node.next = ListNode(lkd_list1[i])
            node = node.next
        pHead2 = None
        if lkd_list2:
            pHead2 = ListNode(lkd_list2[0])
            node = pHead2
        for i in range(1, len(lkd_list2)):
            node.next = ListNode(lkd_list2[i])
            node = node.next
        solution = Solution2()
        rvs_head = solution.Merge(pHead1, pHead2)
        res = list()
        while rvs_head:
            res.append(rvs_head.val)
            rvs_head = rvs_head.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
