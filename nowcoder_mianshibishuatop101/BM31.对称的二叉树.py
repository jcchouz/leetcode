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
# 递归
class Solution:
    def recursion(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.recursion(root1.left, root2.right) and self.recursion(
            root1.right, root2.left
        )

    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        return self.recursion(pRoot, pRoot)
