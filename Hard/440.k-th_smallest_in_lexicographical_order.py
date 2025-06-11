'''
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2025-06-09
'''

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1

        k -= 1
        while k > 0:
            cnt = 0
            intv = [ans, ans + 1]
            while intv[0] <= n:
                cnt += min(n + 1, intv[1]) - intv[0]
                intv = [10 * intv[0], 10 * intv[1]]

            if k >= cnt:
                ans += 1
                k -= cnt

            else:
                ans *= 10
                k -= 1

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findKthNumber(n = 13, k = 2)
    assert test1 == 10

    test2 = sol.findKthNumber(n = 1, k = 1)
    assert test2 == 1
    