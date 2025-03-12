'''
https://leetcode.com/problems/unique-binary-search-trees/
'''
from math import factorial


# https://en.wikipedia.org/wiki/Catalan_number
class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.numTrees(3), 5)