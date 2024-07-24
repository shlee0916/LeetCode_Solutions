'''
https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
'''

from collections import defaultdict

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map_nums = defaultdict(list)

        for num in nums:
            map_num = 0
            for idx, ch in enumerate(str(num)[::-1]):
                map_num += mapping[int(ch)] * 10 ** idx

            map_nums[map_num].append(num)

        ans = []
        for _, nums_lst in sorted(map_nums.items(), key = lambda x: x[0]):
            ans.extend(nums_lst)

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.sortJumbled(mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums = [991, 338, 38])
    assert test1 == [338, 38, 991]

    test2 = sol.sortJumbled(mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums = [789, 456, 123])
    assert test2 == [123, 456, 789]
    