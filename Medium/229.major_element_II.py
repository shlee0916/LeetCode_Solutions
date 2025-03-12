'''
https://leetcode.com/problems/majority-element-ii/description/
'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        return [num for num, freq in count.items() if freq > (len(nums) / 3)]
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.majorityElement([3, 2, 3])
    print(test1, [3])
    assert test1 == [3]
    
    test2 = sol.majorityElement([1])
    print(test2, [1])
    assert test2 == [1]
    
    test3 = sol.majorityElement([1, 2])
    print(test3, [1, 2])
    assert test3 == [1, 2]
    