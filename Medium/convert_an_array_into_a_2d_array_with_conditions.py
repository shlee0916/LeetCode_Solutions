'''
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
'''

from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = Counter(nums)
        new_arr = []
        for _ in range(max(num_count.values())):
            new_row = []
            cur_keys = list(num_count.keys())
            for key in cur_keys:
                new_row.append(key)
                num_count[key] -= 1
                if num_count[key] == 0:
                    num_count.pop(key)

            new_arr.append(new_row)

        return new_arr
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findMatrix(nums = [1, 3, 4, 1, 2, 3, 1])
    assert test1 == [[1, 3, 4, 2], [1, 3], [1]]
    
    test2 = sol.findMatrix(nums = [1, 2, 3, 4])
    assert test2 == [[1, 2, 3, 4]]
    