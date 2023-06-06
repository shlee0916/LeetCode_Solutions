'''
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
'''

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        differ = arr[1] - arr[0]
        
        return all(num == arr[0] + idx * differ for idx, num in enumerate(arr))


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.canMakeArithmeticProgression(arr = [3, 5, 1])
    assert test1 == True

    test2 = sol.canMakeArithmeticProgression(arr = [1, 2, 4])
    assert test2 == False
    