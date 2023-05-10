class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
# 中序遍历，递归+preNode
class Solution:
    def __init__(self):
        self.preNode = None

    def inorder(self, root: TreeNode):
        if not root:
            return
        self.inorder(root.left)
        if self.preNode:
            root.left = self.preNode
            self.preNode.right = root
        self.preNode = root
        self.inorder(root.right)

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.inorder(pRootOfTree)
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
