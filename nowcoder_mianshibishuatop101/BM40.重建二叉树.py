from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param preOrder int整型一维数组
# @param vinOrder int整型一维数组
# @return TreeNode类
#

# 递归
# class Solution:
#     def reConstructBinaryTree(
#         self, preOrder: List[int], vinOrder: List[int]
#     ) -> TreeNode:
#         # write code here
#         if not preOrder:
#             return None
#         root = TreeNode(preOrder[0])
#         tmp = vinOrder.index(preOrder[0])
#         root.left = self.reConstructBinaryTree(preOrder[1 : tmp + 1], vinOrder[:tmp])
#         root.right = self.reConstructBinaryTree(
#             preOrder[tmp + 1 :], vinOrder[tmp + 1 :]
#         )
#         return root


# 双指针
# class Solution:
#     def dfs(
#         self,
#         preStart: int,
#         inStart: int,
#         inEnd: int,
#         preOrder: List[int],
#         vinOrder: List[int],
#     ) -> TreeNode:
#         root = TreeNode(preOrder[0])
#         index = vinOrder.index(preOrder[0])
#         root.left = self.dfs(preStart + 1, inStart, index, preOrder, vinOrder)
#         root.right = self.dfs(
#             preStart + index - inStart + 1, index + 1, inEnd, preOrder, vinOrder
#         )
#         return root
#
#     def reConstructBinaryTree(
#         self, preOrder: List[int], vinOrder: List[int]
#     ) -> TreeNode:
#         self.dfs(0, 0, len(vinOrder) - 1, preOrder, vinOrder)
