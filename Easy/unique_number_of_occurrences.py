'''
https://leetcode.com/problems/unique-number-of-occurrences/description/
'''

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}

        for num in arr:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1

        occ = list(cnt.values())
        arr = []
        for num in occ:
            if num in arr:
                return False
            else:
                arr.append(num)

        return True


# One line
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        return len(set(Counter(arr).values())) == len(set(arr))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.uniqueOccurrences([1,2,2,1,1,3])
    print(test1,True)
    assert test1 == True

    test2 = sol.uniqueOccurrences([1,2])
    print(test2, False)
    assert test2 == False

    test3 = sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    print(test3, True)
    assert test3 == True
