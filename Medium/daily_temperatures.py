'''
https://leetcode.com/problems/daily-temperatures/description/
'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                tmp_idx = stack.pop()
                ans[tmp_idx] = idx - tmp_idx

            stack.append(idx)
                
        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(test1, [1, 1, 4, 2, 1, 1, 0, 0])
    assert test1 == [1, 1, 4, 2, 1, 1, 0, 0]
    
    test2 = sol.dailyTemperatures([30, 40, 50, 60])
    print(test2, [1, 1, 1, 0])
    assert test2 == [1, 1, 1, 0]
    
    test3 = sol.dailyTemperatures([30, 60, 90])
    print(test3, [1, 1, 0])
    assert test3 == [1, 1, 0]
    