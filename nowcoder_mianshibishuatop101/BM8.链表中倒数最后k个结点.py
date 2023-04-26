import traceback


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


# 快慢指针
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        # write code here
        if not pHead:
            return None
        fast = slow = pHead
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


class Solution2:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        # write code here
        if not pHead or not k:
            return None
        stack = list()
        while pHead:
            stack.append(pHead)
            pHead = pHead.next
        if len(stack) < k:
            return None
        node = stack.pop()
        for _ in range(k - 1):
            cur = stack.pop()
            cur.next = node
            node = cur
        return node


while True:
    try:
        # 输入输出
        lkd_list, k = eval(input())
        head = None
        if lkd_list:
            head = ListNode(lkd_list[0])
            cur = head
            for i in range(1, len(lkd_list)):
                cur.next = ListNode(lkd_list[i])
                cur = cur.next
        solution = Solution2()
        res = solution.FindKthToTail(head, k)
        print(res.val)
    except Exception as e:
        print(traceback.format_exc())
        break
