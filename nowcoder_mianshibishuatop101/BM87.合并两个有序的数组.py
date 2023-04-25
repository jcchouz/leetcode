#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
while True:
    try:
        # 输入输出
        strs = input().strip().split('],[')
        A = list(map(int, strs[0][1:].split(',')))
        B = list(map(int, strs[1][:-1].split(',')))
        m = len(A)
        n = len(B)
        A += [0 for _ in range(n)]
        # 算法
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                k -= 1
                i -= 1
            else:
                A[k] = B[j]
                k -= 1
                j -= 1
        if i < 0:
            while j >= 0:
                A[k] = B[j]
                k -= 1
                j -= 1
        print(A)
    except:
        print("error.")
        break


#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
# class Solution:
#     def merge(self, A, m, B, n):
#         # write code here
#         i = m - 1
#         j = n - 1
#         k = m + n - 1
#         while i >= 0 and j >= 0:
#             if A[i] > B[j]:
#                 A[k] = A[i]
#                 k -= 1
#                 i -= 1
#             else:
#                 A[k] = B[j]
#                 k -= 1
#                 j -= 1
#         if i < 0:
#             while j >= 0:
#                 A[k] = B[j]
#                 k -= 1
#                 j -= 1
#         return A


# if __name__ == '__main__':
#     while True:
#         try:
#             strs = input().strip().split('],[')
#             A = list(map(int, strs[0][1:].split(',')))
#             B = list(map(int, strs[1][:-1].split(',')))
#             m = len(A)
#             n = len(B)
#             A += [0 for _ in range(n)]
#             solution = Solution()
#             res = solution.merge(A, m, B, n)
#         except:
#             print("error.")
#             break
