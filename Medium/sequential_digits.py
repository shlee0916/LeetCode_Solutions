'''
https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02
'''

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for num in range(1, 9):
            next_num = num
            while num <= high and next_num < 10:
                if num >= low:
                    ans.append(num)

                next_num += 1
                num = num * 10 + next_num

        return sorted(ans)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.sequentialDigits(low = 100, high = 300)
    assert test1 == [123, 234]

    test2 = sol.sequentialDigits(low = 1000, high = 13000)
    assert test2 == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    