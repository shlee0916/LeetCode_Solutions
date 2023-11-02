'''
https://leetcode.com/problems/maximum-score-from-removing-stones/description/
'''

from heapq import heapify, heappop, heappush


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapify(heap)

        score = 0
        while heap and len(heap) > 1:
            first_pile = heappop(heap)
            second_pile = heappop(heap)

            if first_pile <= 0 and second_pile <= 0:
                first_pile += 1
                second_pile += 1
                score += 1

            if first_pile < 0:
                heappush(heap, first_pile)
            if second_pile < 0:
                heappush(heap, second_pile)

        return score


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumScore(a = 2, b = 4, c = 6)
    assert test1 == 6

    test2 = sol.maximumScore(a = 4, b = 4, c = 6)
    assert test2 == 7

    test3 = sol.maximumScore(a = 1, b = 8, c = 8)
    assert test3 == 8
    