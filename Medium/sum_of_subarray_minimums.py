'''
https://leetcode.com/problems/sum-of-subarray-minimums/
'''
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        res = [0] * len(arr)
        stack = [0]
        for idx, num in enumerate(arr):
            while arr[stack[-1]] > num:
                stack.pop()
                
            res[idx] = res[stack[-1]] + (idx - stack[-1]) * num
            stack.append(idx)
            
        return sum(res) % (10 ** 9 + 7)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sumSubarrayMins([3, 1, 2, 4])
    print(test1, 17)
    assert test1 == 17
    
    test2 = sol.sumSubarrayMins([11, 81, 94, 43, 3])
    print(test2, 444)
    assert test2 == 444
    