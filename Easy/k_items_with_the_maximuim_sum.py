'''
https://leetcode.com/problems/k-items-with-the-maximum-sum/
'''

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return min(k, numOnes) - max(0, k - numOnes - numZeros)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2)
    assert test1 == 2
    
    test2 = sol.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4)
    assert test2 == 3
    