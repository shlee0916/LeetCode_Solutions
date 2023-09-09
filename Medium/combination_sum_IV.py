'''
https://leetcode.com/problems/combination-sum-iv/description/?envType=daily-question&envId=2023-09-09
'''

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb_sum = {}
        comb_sum[0] = 1

        def search(target):
            if target in comb_sum:
                return comb_sum[target]

            num_sum = 0
            for num in nums:
                if target > num:
                    num_sum += search(target - num)
                elif target == num:
                    num_sum += 1

            comb_sum[target] = num_sum

            return num_sum

        return search(target)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.combinationSum4(nums = [1, 2, 3], target = 4)
    assert test1 == 7
    
    test2 = sol.combinationSum4(nums = [9], target = 3)
    assert test2 == 0
    