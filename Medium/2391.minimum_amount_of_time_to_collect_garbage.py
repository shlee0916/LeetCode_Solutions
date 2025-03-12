'''
https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/
'''

from typing import List


class Solution:
    def garbageCollection(self,  garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        paper_end = 0
        glass_end = 0
        metal_end = 0

        for idx, gbg in enumerate(garbage):
            if "P" in gbg:
                paper_end = idx
            if "G" in gbg:
                glass_end = idx
            if "M" in gbg:
                metal_end = idx

            total_time += len(gbg)

        for end in [paper_end, glass_end, metal_end]:
            total_time += sum(travel[:end])

        return total_time
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.garbageCollection(garbage = ["G", "P", "GP", "GG"], travel = [2, 4, 3])
    print(test1, 21)
    assert test1 == 21

    test2 = sol.garbageCollection(garbage = ["MMM", "PGM", "GP"], travel = [3, 10])
    print(test2, 37)
    assert test2 == 37
    