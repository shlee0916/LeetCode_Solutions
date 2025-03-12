'''
https://leetcode.com/problems/most-beautiful-item-for-each-query/?envType=daily-question&envId=2024-11-12
'''

from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = []

        items.sort()
        for idx in range(1, len(items)):
            items[idx][1] = max(items[idx][1], items[idx - 1][1])

        for query in queries:
            left = 0
            right = len(items) - 1

            while left <= right:
                mid = (left + right) >> 1
                price, beauty = items[mid]

                if price > query:
                    right = mid - 1
                else:
                    left = mid + 1

            ans.append(items[right][1] if right >= 0 else 0)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumBeauty(items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries = [1, 2, 3, 4, 5, 6])
    assert test1 == [2, 4, 5, 5, 6, 6]

    test2 = sol.maximumBeauty(items = [[1, 2], [1, 2], [1, 3], [1, 4]], queries = [1])
    assert test2 == [4]

    test3 = sol.maximumBeauty(items = [[10, 1000]], queries = [5])
    assert test3 == [0]
