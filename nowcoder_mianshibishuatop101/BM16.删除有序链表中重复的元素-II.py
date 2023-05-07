import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        res = ListNode(-1)
        res.next = head
        cur = res
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                tmp = cur.next.val
                while cur.next != None and cur.next.val == tmp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next
