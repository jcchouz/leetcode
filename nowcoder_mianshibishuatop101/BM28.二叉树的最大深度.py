import queue


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
# @return int整型
#
# DFS，递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # write code here
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# BFS，队列
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # write code here
        res = 0
        if not root:
            return res
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            res += 1
            for _ in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return res
