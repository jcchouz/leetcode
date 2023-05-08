from typing import List
import sys


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
# @return int整型一维数组
#
class Solution:
    def __init__(self):
        self.res = list()

    def inorfer(self, root: TreeNode):
        if not root:
            return None
        self.inorfer(root.left)
        self.res.append(root.val)
        self.inorfer(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        sys.setrecursionlimit(3000)
        self.inorfer(root)
        return self.res
