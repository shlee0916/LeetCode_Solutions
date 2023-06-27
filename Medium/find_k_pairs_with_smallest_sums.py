'''
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
'''

from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        if not nums1 or not nums2 or not k:
            return ans

        heap = []
        visit = set((0, 0))

        heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while len(ans) < k and heap:
            _, idx_num1, idx_num2 = heappop(heap)
            ans.append([nums1[idx_num1], nums2[idx_num2]])

            if idx_num1 + 1 < len(nums1) and (idx_num1 + 1, idx_num2) not in visit:
                heappush(heap, (nums1[idx_num1 + 1] + nums2[idx_num2], idx_num1 + 1, idx_num2))
                visit.add((idx_num1 + 1, idx_num2))

            if idx_num2 + 1 < len(nums2) and (idx_num1, idx_num2 + 1) not in visit:
                heappush(heap, (nums1[idx_num1] + nums2[idx_num2 + 1], idx_num1, idx_num2 + 1))
                visit.add((idx_num1, idx_num2 + 1))

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.kSmallestPairs(nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3)
    assert test1 == [[1, 2], [1, 4], [1, 6]]

    test2 = sol.kSmallestPairs(nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2)
    assert test2 == [[1, 1], [1, 1]]
    
    test3 = sol.kSmallestPairs(nums1 = [1, 2], nums2 = [3], k = 3)
    assert test3 == [[1, 3], [2, 3]]
    