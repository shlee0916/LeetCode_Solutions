'''
https://leetcode.com/problems/closest-prime-numbers-in-range/?envType=daily-question&envId=2025-03-07
'''

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Make sieve of eratosthenes
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        for num, is_prime in enumerate(sieve):
            if is_prime:
                for num in range(num * num, right + 1, num):
                    sieve[num] = False

        # re-arrange primes
        primes = [num for num in range(left, right + 1) if sieve[num]]

        # Find answer
        min_diff = float("inf")
        ans = [-1, -1]
        for idx in range(1, len(primes)):
            cur_diff = primes[idx] - primes[idx - 1]
            if cur_diff < min_diff:
                ans = [primes[idx - 1], primes[idx]]
                min_diff = cur_diff

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.closestPrimes(left = 10, right = 19)
    assert test1 == [11, 13]

    test2 = sol.closestPrimes(left = 4, right = 6)
    assert test2 == [-1, -1]
    