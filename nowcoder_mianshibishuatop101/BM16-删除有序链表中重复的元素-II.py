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
        while not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
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
