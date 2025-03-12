'''
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/
'''

from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left_bag_sizes = [capa - rock for capa, rock in zip(capacity, rocks)]
        left_bag_sizes.sort()   

        cnt = 0
        for left_size in left_bag_sizes:
            additionalRocks -= left_size
            if additionalRocks < 0:
                break
            else:
                cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumBags(capacity = [2, 3, 4, 5], rocks = [1, 2, 4, 4], additionalRocks = 2)
    assert test1 == 3

    test2 = sol.maximumBags(capacity = [10, 2, 2], rocks = [2, 2, 0], additionalRocks = 100)
    assert test2 == 3
    