'''
https://leetcode.com/problems/relative-ranks/?envType=daily-question&envId=2024-05-08
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        heap = []
        for idx, val in enumerate(score):
            heappush(heap, (-val, idx))

        rank = 0
        while heap:
            _, idx = heappop(heap)
            if rank < 3:
                if rank == 0:
                    ans[idx] = "Gold Medal"
                elif rank == 1:
                    ans[idx] = "Silver Medal"
                elif rank == 2:
                    ans[idx] = "Bronze Medal"
            else:
                ans[idx] = f"{rank + 1}"
            rank += 1

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findRelativeRanks(score = [5, 4, 3, 2, 1])
    assert test1 == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    test2 = sol.findRelativeRanks(score = [10, 3, 8, 9, 4])
    assert test2 == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    