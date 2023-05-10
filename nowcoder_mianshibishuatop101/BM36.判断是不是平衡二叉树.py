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
# @return bool布尔型
#
# 层序遍历，队列
import queue


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # write code here
        if not root:
            return True
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            root = q.get()
            if not root:
                while not q.empty():
                    if q.get():
                        return False
            else:
                q.put(root.left)
                q.put(root.right)
        return True
