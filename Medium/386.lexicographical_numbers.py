'''
https://leetcode.com/problems/lexicographical-numbers/description/
'''

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(number) for number in range(1, n + 1)]
        nums.sort()
        
        return list(map(int, nums))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.lexicalOrder(13)
    print(test1, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])
    assert test1 == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

    test2 = sol.lexicalOrder(2)
    print(test2, [1, 2])
    assert test2 == [1, 2]
