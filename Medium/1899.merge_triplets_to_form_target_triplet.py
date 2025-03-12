'''
https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
'''

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0, 0, 0]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                ans[0] = max(ans[0], triplet[0])
                ans[1] = max(ans[1], triplet[1])
                ans[2] = max(ans[2], triplet[2])
        
        return ans == target


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.mergeTriplets(triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], target = [2, 7, 5])
    assert test1 == True

    test2 = sol.mergeTriplets(triplets = [[3, 4, 5], [4, 5, 6]], target = [3, 2, 5])
    assert test2 == False

    test3 = sol.mergeTriplets(triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target = [5, 5, 5])
    assert test3 == True
    