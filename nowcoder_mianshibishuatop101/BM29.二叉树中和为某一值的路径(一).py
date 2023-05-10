import queue
import traceback


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
# @param sum int整型
# @return bool布尔型
#
# 递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # write code here
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val
        )


def Serialize(root):
    # write code here
    if not root:
        return
    emptyNode = TreeNode("#")
    res = []
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        tmp = q.get()
        res.append(str(tmp.val))
        if tmp != emptyNode:
            if tmp.left:
                q.put(tmp.left)
            else:
                q.put(emptyNode)
            if tmp.right:
                q.put(tmp.right)
            else:
                q.put(emptyNode)
    return ",".join(res)


def Deserialize(s):
    # write code here
    if not s:
        return
    sl = s.split(",")
    n = len(sl)
    root = TreeNode(int(sl[0]))
    q = queue.Queue()
    q.put(root)
    for i in range(1, n, 2):
        node = q.get()
        a, b = sl[i], sl[i + 1]
        if a != "#":
            node.left = TreeNode(int(a))
            q.put(node.left)
        if b != "#":
            node.right = TreeNode(int(b))
            q.put(node.right)
    return root


while True:
    try:
        tree, sum = input().split("}")
        root = Deserialize(tree[1:])
        solution = Solution()
        print(solution.hasPathSum(root, int(sum[1:])))
    except Exception as e:
        print(traceback.format_exc())
        break
