'''
https://leetcode.com/problems/count-primes/
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True] * n

        for idx in range(2, n):
            if sieve[idx] == True:
                for false_idx in range(idx + idx, n, idx):
                    sieve[false_idx] = False

        return len([idx for idx in range(2, n) if sieve[idx] == True])


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countPrimes(n = 10)
    assert test1 == 4
    
    test2 = sol.countPrimes(n = 0)
    assert test2 == 0
    
    test3 = sol.countPrimes(n = 1)
    assert test3 == 0
    