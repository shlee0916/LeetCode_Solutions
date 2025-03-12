'''
https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/
'''

from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()
        for num in nums:
            ans.add(num)
            reverse = str(num)[::-1]
            ans.add(int(reverse))

        return len(ans)
    
    def countDistinctIntegers_oneline(self, nums: List[int]) -> int:
        return len(set(nums + [int(val[::-1]) for val in list(map(str, nums))]))
    
    
if __name__ == "__main__":
    sol = Solution()
    
    # Test1
    assert sol.countDistinctIntegers(nums = [1, 13, 10, 12, 31]) == 6
    assert sol.countDistinctIntegers_oneline(nums = [1, 13, 10, 12, 31]) == 6
    
    # Test2
    assert sol.countDistinctIntegers(nums = [2, 2, 2]) == 1
    assert sol.countDistinctIntegers_oneline(nums = [2, 2, 2]) == 1
    