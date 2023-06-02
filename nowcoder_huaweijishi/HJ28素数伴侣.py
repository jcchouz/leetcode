import math
import traceback

from typing import List


# 验证是否为质数
def check(num: int):
    for i in range(2, int(math.sqrt(num)) + 2):
        if not num % i:
            return False
    return True


# 配对，寻找与奇数对应的偶数
def find(o: int, even: List[int], visited: List[int], choose: List[int]):
    for i in range(len(even)):
        if check(o + even[i]) and not visited[i]:
            visited[i] = 1
            if not choose[i] or find(choose[i], even, visited, choose):
                choose[i] = o
                return True
    return False


while True:
    try:
        # 输入
        n = input()
        l = list(map(int, input().split()))

        # 分为奇数和偶数
        odd = list()
        even = list()
        for i in l:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)

        # 存放配对
        choose = [0] * len(even)
        # 判断是否可以
        for o in odd:
            visited = [0] * len(even)
            find(o, even, visited, choose)
        # 计算对数
        cnt = 0
        for i in choose:
            if i:
                cnt += 1
        print(cnt)
    except Exception as e:
        print(traceback.format_exc())
        break

'''
import math
def check(n): #判断是否是素数
    for i in range(2,int(math.sqrt(n)) + 2): #除去1和本身的数没有其他的因子称为素数，但其实检验到int(math.sqrt(n)) + 1即可（数学证明略），不然会超时
        if(n % i == 0):
            return False
    return True

def find(odd, visited, choose, evens): #配对的过程
    for j,even in enumerate(evens):  
        if check(odd+even) and not visited[j]: #如果即能配对，这两个数之前没有配过对（即使两个不能配对visit值为0，但是也不能过是否是素数这一关，所以visit就可以
        看为两个能配对的素数是否能配对）
            visited[j] = True #代表这两个数能配对
            if choose[j]==0 or find(choose[j],visited,choose,evens): #如果当前奇数没有和任何一个偶数现在已经配对，那么认为找到一组可以连接的，如果当前的奇数
            已经配对，那么就让那个与之配对的偶数断开连接，让他再次寻找能够配对的奇数
                choose[j] = odd #当前奇数已经和当前的偶数配对
                return True 
    return False 如果当前不能配对则返回False

while True:
    try:
        n = int(input())
        a = input()
        a = a.split()
        b = []
        count = 0
        for i in range(len(a)):
            a[i] = int(a[i])
        evens = []
        odds = []
        for i in a: #将输入的数分为奇数和偶数
            if(i % 2 == 0):
                odds.append(i)
            else:
                evens.append(i)
        choose = [0]*len(evens) #choose用来存放当前和这个奇数配对的那个偶数
        for odd in odds:
            visited = [False]*len(evens) #visit用来存放当前奇数和偶数是否已经配过对
            if find(odd,visited,choose,evens):
                count += 1
        print(count)
    except:
        break
'''
