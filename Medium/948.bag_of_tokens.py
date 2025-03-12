'''
https://leetcode.com/problems/bag-of-tokens/
'''

from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        max_score = 0
        cur_score = 0
        cur_power = power
        left = 0
        right = len(tokens) - 1

        while left <= right:
            if tokens[left] <= cur_power:
                cur_power -= tokens[left]
                cur_score += 1
                max_score = max(cur_score, max_score)
                left += 1
            elif cur_score > 0:
                cur_score -= 1
                cur_power += tokens[right]
                right -= 1
            else:
                break

        return max_score


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.bagOfTokensScore(tokens = [100], power = 50)
    assert test1 == 0
    
    test2 = sol.bagOfTokensScore(tokens = [200, 100], power = 150)
    assert test2 == 1
    
    test3 = sol.bagOfTokensScore(tokens = [100, 200, 300, 400], power = 200)
    assert test3 == 2
    