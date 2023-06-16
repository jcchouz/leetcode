from cmath import phase
import traceback
from typing import List


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 双指针
class Solution:
    def EntryNodeOfLoop(self, pHead) -> ListNode:
        # write code here
        if not pHead:
            return None
        slow = fast = pHead
        while fast:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                break
        slow = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


# 哈希表
class Solution2:
    def EntryNodeOfLoop(self, pHead) -> ListNode:
        # write code here
        if not pHead:
            return None
        hashmap = set()
        while pHead:
            if pHead in hashmap:
                return pHead
            hashmap.add(pHead)
            pHead = pHead.next
        return None


while True:
    try:
        # 输入输出
        lkd_list1, lkd_list2 = eval(input())
        head1 = head2 = None
        if lkd_list1:
            head1 = ListNode(lkd_list1[0])
            cur = head1
            for i in range(1, len(lkd_list1)):
                cur.next = ListNode(lkd_list1[i])
                cur = cur.next
            tmp = cur
        if lkd_list2:
            head2 = ListNode(lkd_list2[0])
            cur = head2
            for i in range(1, len(lkd_list2)):
                cur.next = ListNode(lkd_list2[i])
                cur = cur.next
            cur.next = head2
        if lkd_list1:
            tmp.next = head2
        else:
            head1 = head2
        solution = Solution()
        res = solution.EntryNodeOfLoop(head1)
        print(res.val)
    except Exception as e:
        print(traceback.format_exc())
        break
