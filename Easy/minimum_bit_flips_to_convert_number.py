'''
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/?envType=daily-question&envId=2024-09-11
'''

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        differ = start ^ goal
        ans = 0

        while differ > 0:
            ans += differ & 1
            differ >>= 1

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minBitFlips(start = 10, goal = 7)
    assert test1 == 3

    test2 = sol.minBitFlips(start = 3, goal = 4)
    assert test2 == 3
    