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
# @param p int整型
# @param q int整型
# @return int整型
#
# 迭代，找路径，最后一个公共节点
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        pass


# 递归
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        if not root:
            return -1
        if (p <= root.val <= q) or (q <= root.val <= root.val):
            return root.val
        if p <= root.val and q <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
