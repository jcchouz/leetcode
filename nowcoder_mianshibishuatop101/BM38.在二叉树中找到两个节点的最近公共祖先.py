class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
# 递归
class Solution:
    def recursion(self, root: TreeNode, o1: int, o2: int):
        if not root or root.val == o1 or root.val == o2:
            return root
        l = self.recursion(root.left, o1, o2)
        r = self.recursion(root.right, o1, o2)
        if not l:
            return r
        if not r:
            return l
        return root

    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        # write code here
        return self.recursion(root, o1, o2).val


# BFS，层序遍历+hashmap
import queue


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        # write code here
        hmap = dict()
        tmp = set()
        hmap[root.val] = -1
        q = queue.Queue()
        q.put(root)
        while o1 not in hmap or o2 not in hmap:
            root = q.get()
            if root.left:
                hmap[root.left.val] = root.val
                q.put(root.left)
            if root.right:
                hmap[root.right.val] = root.val
                q.put(root.right)
        while o1 >= 0:
            tmp.add(o1)
            o1 = hmap[o1]
        while o2 not in tmp:
            o2 = hmap[o2]
        return o2
