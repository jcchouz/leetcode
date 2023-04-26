import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 双指针
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # write code here
        if not head:
            return False
        fast = slow = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False


# 哈希表
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        # write code here
        if not head:
            return False
        hashmap = set()
        while head:
            if head in hashmap:
                return True
            hashmap.add(head)
            head = head.next
        return False


while True:
    try:
        # 输入输出
        lkd_lists, cycle = eval(input())
        head = None
        flag = None
        if lkd_lists:
            head = ListNode(lkd_lists[0])
            cur = head
            for i in range(1, len(lkd_lists)):
                cur.next = ListNode(lkd_lists[i])
                cur = cur.next
                if i == cycle:
                    flag = cur
            cur.next = flag
        solution = Solution()
        res = solution.hasCycle(head)
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
