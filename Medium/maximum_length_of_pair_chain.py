'''
https://leetcode.com/problems/maximum-length-of-pair-chain/
'''

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda pair: pair[1])
        
        ans = 0
        cur = -float("inf")
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findLongestChain(pairs = [[1, 2], [2, 3], [3, 4]])
    assert test1 == 2
    
    test2 = sol.findLongestChain(pairs = [[1,2],[7,8],[4,5]])
    assert test2 == 3
    