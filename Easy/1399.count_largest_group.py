'''
https://leetcode.com/problems/count-largest-group/?envType=daily-question&envId=2025-04-23
'''

class Solution:
    def countLargestGroup(self, n: int) -> int:
        past_sum = {0: 0}
        cnts = [0] * (4 * 9)

        for num in range(1, n + 1):
            quotient, remainder = divmod(num, 10)
            past_sum[num] = past_sum[quotient] + remainder
            cnts[past_sum[num] - 1] += 1

        return cnts.count(max(cnts))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countLargestGroup(n = 13)
    assert test1 == 4

    test2 = sol.countLargestGroup(n = 2)
    assert test2 == 2
    