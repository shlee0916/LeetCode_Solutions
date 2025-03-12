'''
https://leetcode.com/problems/find-original-array-from-doubled-array/
'''
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        stack = []
        
        for num in changed:
            if stack and stack[0] * 2 == num:
                ans.append(stack.pop(0))
            else:
                stack.append(num)
                
        return ans if not stack else None
    
    
if __name__ == "__main__":
    sol = Solution()
        
    print(sol.findOriginalArray([1, 3, 4, 2, 6, 8]), [1, 3, 4])
    print(sol.findOriginalArray([6, 3, 0, 1]), [])
    print(sol.findOriginalArray([1]), [])
    print(sol.findOriginalArray([2, 1]), [1])
    print(sol.findOriginalArray([1, 3, 4, 2, 6]), [])