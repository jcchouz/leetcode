import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 快慢指针
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # write code here
        if not head:
            return None
        fast = slow = head
        for _ in range(n + 1):
            if not fast:
                return head.next
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


while True:
    try:
        # 输入输出
        lkd_list, n = eval(input())
        head = None
        if lkd_list:
            head = ListNode(lkd_list[0])
            cur = head
            for i in range(1, len(lkd_list)):
                cur.next = ListNode(lkd_list[i])
                cur = cur.next
        solution = Solution()
        res = solution.removeNthFromEnd(head, n)
        while res:
            print(res.val)
    except Exception as e:
        print(traceback.format_exc())
        break
