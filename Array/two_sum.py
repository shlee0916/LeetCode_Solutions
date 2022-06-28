from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in nums and nums.index(remain) != idx:
                result = [idx, nums.index(target - num)]
        
        return  result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    nums = [2, 7, 11, 15]
    target = 9
    
    print(sol.twoSum(nums, target))