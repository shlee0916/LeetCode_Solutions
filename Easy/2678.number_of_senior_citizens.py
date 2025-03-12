'''
https://leetcode.com/problems/number-of-senior-citizens/?envType=daily-question&envId=2024-08-01
'''

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for info in details:
            if int(info[11:13]) > 60:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countSeniors(details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"])
    assert test1 == 2

    test2 = sol.countSeniors(details = ["1313579440F2036", "2921522980M5644"])
    assert test2 == 0
    