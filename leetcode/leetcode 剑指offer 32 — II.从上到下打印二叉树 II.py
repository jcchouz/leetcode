# Definition for a binary tree node.
import queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        # BFS
        res = list()
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            res.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return res
