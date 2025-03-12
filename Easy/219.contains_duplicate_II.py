'''
https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for idx, num in enumerate(nums):
            if num in seen:
                return True

            seen.add(num)

            if len(seen) > k:
                seen.remove(nums[idx - k])
        
        return False


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.containsNearbyDuplicate(nums = [1, 2, 3, 1], k = 3)
    assert test1 == True
    
    test2 = sol.containsNearbyDuplicate(nums = [1, 0, 1, 1], k = 1)
    assert test2 == True
    
    test3 = sol.containsNearbyDuplicate(nums = [1, 2, 3, 1, 2, 3], k = 2)
    assert test3 == False
    