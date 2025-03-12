'''
https://leetcode.com/problems/3sum-closest/
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            
            cur = sum(nums[:3])
            if cur >= target:
                return cur

            cur = sum(nums[-3:])
            if cur < target:
                return cur
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                if curSum == target:
                    return target
                if abs(curSum-target) < abs(result-target):
                    result = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.threeSumClosest([-1, 2, 1, -4], 1), 2)