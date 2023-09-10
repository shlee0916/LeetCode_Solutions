'''
https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=daily-question&envId=2023-09-10
'''

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * (length + 1)

        for idx in range(length - 1, -1, -1):
            point = questions[idx][0]
            jump = questions[idx][1]

            next_one = min(length, idx + jump + 1)
            dp[idx] = max(dp[idx + 1], point + dp[next_one])

        return dp[0]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.mostPoints(questions = [[3, 2], [4, 3], [4, 4], [2, 5]])
    assert test1 == 5
    
    test2 = sol.mostPoints(questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
    assert test2 == 7
    