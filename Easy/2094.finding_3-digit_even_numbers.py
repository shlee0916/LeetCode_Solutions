'''
https://leetcode.com/problems/finding-3-digit-even-numbers/?envType=daily-question&envId=2025-05-12
'''

from collections import Counter

from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_cnts = Counter(digits)
        ans = []
        for num in range(100, 1000, 2):
            num_cnts = Counter(map(int, str(num)))

            if all(cnt <= digit_cnts[num] for num, cnt in num_cnts.items()):
                ans.append(num)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findEvenNumbers(digits = [2, 1, 3, 0])
    assert test1 == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

    test2 = sol.findEvenNumbers(digits = [2, 2, 8, 8, 2])
    assert test2 == [222, 228, 282, 288, 822, 828, 882]

    test3 = sol.findEvenNumbers(digits = [3, 7, 5])
    assert test3 == []
