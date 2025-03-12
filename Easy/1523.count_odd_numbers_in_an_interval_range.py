'''
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = (high - low) // 2

        return cnt + 1 if low % 2 != 0 or high % 2 != 0 else cnt


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countOdds(low = 3, high = 7)
    print(test1, 3)
    assert test1 == 3

    test2 = sol.countOdds(low = 8, high = 10)
    print(test2, 1)
    assert test2 == 1
    