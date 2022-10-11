'''
https://leetcode.com/problems/increasing-triplet-subsequence/
'''
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
            
        return False


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.increasingTriplet([1, 2, 3, 4, 5]), True)
    print(sol.increasingTriplet([1, 2, 2, 1]), False)