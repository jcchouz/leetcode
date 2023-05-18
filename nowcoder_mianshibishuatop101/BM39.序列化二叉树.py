class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS，层序遍历，队列
import queue


class Solution:
    def Serialize(self, root):
        # write code here
        # write code here
        if not root:
            return None
        res = list()
        emptyNode = TreeNode(-1)
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            root = q.get()
            res.append(root.val)
            if root != emptyNode:
                if root.left:
                    q.put(root.left)
                else:
                    q.put(emptyNode)
                if root.right:
                    q.put(root.right)
                else:
                    q.put(emptyNode)
        res = list(map(str, res))
        return ",".join(res)

    def Deserialize(self, s: str):
        # write code here
        if not s:
            return None
        tmp = s.split(",")
        tmp = list(map(int, tmp))
        root = TreeNode(tmp[0])
        q = queue.Queue()
        q.put(root)
        for i in range(1, len(tmp), 2):
            node = q.get()
            l = TreeNode(tmp[i]) if tmp[i] >= 0 else None
            r = TreeNode(tmp[i + 1]) if tmp[i + 1] >= 0 else None
            if l:
                node.left = l
                q.put(l)
            if r:
                node.right = r
                q.put(r)
        return root
