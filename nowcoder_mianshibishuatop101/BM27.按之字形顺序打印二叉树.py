from typing import List
import sys
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
# @return int整型二维数组
#
class Solution:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        # write code here
        if not pRoot:
            return None
        q = queue.Queue()
        res = list()
        q.put(pRoot)
        i = 0
        while not q.empty():
            tmp = list()
            for _ in range(q.qsize()):
                node = q.get()
                tmp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if i % 2:
                tmp = tmp[::-1]
            res.append(tmp)
            i += 1
        return res
