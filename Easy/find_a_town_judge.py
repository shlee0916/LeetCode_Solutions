'''
https://leetcode.com/problems/find-the-town-judge/submissions/883659372/
'''

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustee = [0] * (n + 1)

        for person, trust_person in trust:
            trustee[person] -= 1
            trustee[trust_person] += 1

        for idx, person in enumerate(trustee[1:]):
            if person == n - 1:
                return idx + 1

        return -1
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findJudge(n = 2, trust = [[1, 2]])
    print(test1, 2)
    assert test1 == 2
    
    test2 = sol.findJudge(n = 3, trust = [[1, 3], [2, 3]])
    print(test2, 3)
    assert test2 == 3
    
    test3 = sol.findJudge(n = 3, trust = [[1, 3], [2, 3], [3, 1]])
    print(test3, -1)
    assert test3 == -1
