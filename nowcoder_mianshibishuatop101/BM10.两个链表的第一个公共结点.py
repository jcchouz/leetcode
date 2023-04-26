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
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1 = pHead1
        l2 = pHead2
        while l1 != l2:
            l1 = l1.next if l1 else pHead2
            l2 = l2.next if l2 else pHead1
        return l1


while True:
    try:
        # 输入输出
        l1, l2, l3 = eval(input())
        head1 = head2 = head3 = None
        if l3:
            head3 = ListNode(l3[0])
            cur = head3
            for i in range(1, len(l3)):
                cur.next = ListNode(l3[i])
                cur = cur.next
        if l1:
            head1 = ListNode(l1[0])
            cur = head1
            for i in range(1, len(l1)):
                cur.next = ListNode(l1[i])
                cur = cur.next
            cur.next = head3
        if l2:
            head2 = ListNode(l2[0])
            cur = head2
            for i in range(1, len(l2)):
                cur.next = ListNode(l2[i])
                cur = cur.next
            cur.next = head3
        solution = Solution()
        node = solution.FindFirstCommonNode(head1, head2)
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)
    except Exception as e:
        print(traceback.format_exc())
        break
