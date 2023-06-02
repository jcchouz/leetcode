import math
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if is_primes[i] == 1:
                is_primes[i**2 : n : i] = [0] & len(is_primes[i**2 : n : i])
        return sum(is_primes)


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(2))


'''
        if n < 2: return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)

作者：powcai
链接：https://leetcode.cn/problems/count-primes/solution/qiu-zhi-shu-chao-guo-90-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

'''
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [1] * n
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1: res += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return res

作者：powcai
链接：https://leetcode.cn/problems/count-primes/solution/qiu-zhi-shu-chao-guo-90-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


'''
class Solution {
public:
    bool isPrime(int x) {
        for (int i = 2; i * i <= x; ++i) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    int countPrimes(int n) {
        int ans = 0;
        for (int i = 2; i < n; ++i) {
            ans += isPrime(i);
        }
        return ans;
    }
};

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/count-primes/solution/ji-shu-zhi-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
'''
class Solution {
public:
    int countPrimes(int n) {
        vector<int> isPrime(n, 1);
        int ans = 0;
        for (int i = 2; i < n; ++i) {
            if (isPrime[i]) {
                ans += 1;
                if ((long long)i * i < n) {
                    for (int j = i * i; j < n; j += i) {
                        isPrime[j] = 0;
                    }
                }
            }
        }
        return ans;
    }
};

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/count-primes/solution/ji-shu-zhi-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
