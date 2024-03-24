'''
https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        height_len = len(height)

        max_left = height[0]
        max_right = height[height_len - 1]

        left_idx = 1
        right_idx = height_len - 2

        ans = 0
        while left_idx <= right_idx:
            if max_left < max_right:
                if height[left_idx] > max_left:
                    max_left = height[left_idx]
                else:
                    ans += max_left - height[left_idx]
                left_idx += 1
            else:
                if height[right_idx] > max_right:
                    max_right = height[right_idx]
                else:
                    ans += max_right - height[right_idx]
                right_idx -= 1
            
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.trap(height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert test1 == 6
    
    test2 = sol.trap(height = [4, 2, 0, 3, 2, 5])
    assert test2 == 9
    