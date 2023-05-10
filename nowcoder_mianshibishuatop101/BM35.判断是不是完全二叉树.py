class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
# 递归，DFS，自顶向下
class Solution:
    def __init__(self):
        self.hmap = dict()

    def depth(self, root: TreeNode):
        if not root:
            return 0
        tmp = max(self.depth(root.left), self.depth(root.right)) + 1
        self.hmap[root] = tmp
        return tmp

    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        self.depth(pRoot)
        l = self.hmap[pRoot.left] if pRoot.left else 0
        r = self.hmap[pRoot.right] if pRoot.right else 0
        return (
            abs(l - r) <= 1
            and self.IsBalanced_Solution(pRoot.left)
            and self.IsBalanced_Solution(pRoot.right)
        )


# 递归，DFS，自底向上
class Solution:
    def depth(self, root: TreeNode):
        if not root:
            return 0
        l = self.depth(root.left)
        if l == -1:
            return -1
        r = self.depth(root.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1

    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        # write code here
        return self.depth(pRoot) != -1
