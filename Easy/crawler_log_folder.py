'''
https://leetcode.com/problems/crawler-log-folder/?envType=daily-question&envId=2024-07-10
'''

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if ".." in log:
                depth -= 1 if depth > 0 else 0
            elif "." in log:
                pass
            else:
                depth += 1

        return depth


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(logs = ["d1/", "d2/", "../", "d21/", "./"])
    assert test1 == 2

    test2 = sol.minOperations(logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"])
    assert test2 == 3

    test3 = sol.minOperations(logs = ["d1/", "../", "../", "../"])
    assert test3 == 0
    